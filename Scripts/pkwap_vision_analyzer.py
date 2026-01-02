#!/usr/bin/env python3
"""
PK-WAP Vision Analyzer - Validates text-only analysis against image+text analysis

This script generates PK-WAP memos using GPT-4o vision capabilities to analyze
both PNG scans AND extracted text from transcripts. Used to validate whether
image analysis provides meaningful additional insights.

Usage:
  python3 pkwap_vision_analyzer.py --case P93-G1-S4 --compare

Requirements:
  - OPENROUTER_API_KEY in environment or .env file
  - PNG scans in Data/Raw/Raw PNG files/
  - Naming_CodesDONOT_TRASH.csv for code-to-folder mapping
"""

import argparse
import sys
import time
import os
import base64
import csv
from pathlib import Path
from typing import Optional, List, Dict
import json

# Load .env file if present
env_file = Path(__file__).parent.parent / ".env"
if env_file.exists():
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                os.environ.setdefault(key.strip(), value.strip())

try:
    from openai import OpenAI
except ImportError:
    print("Error: OpenAI package not installed.")
    print("Install with: pip install openai")
    sys.exit(1)

# Configuration
DEFAULT_MODEL = "openai/gpt-4o"
DEFAULT_TEMPERATURE = 0.2
DEFAULT_MAX_TOKENS = 16000

# Paths - adjust these as needed
CHAPTER_REPO = Path("/home/todd/TEA-repos/TEA-Taylor-Series-Chapter")
PAPER_REPO = Path("/home/todd/TEA-repos/TEA-Taylor-Series-Paper")
PNG_DIR = CHAPTER_REPO / "Data/Raw/Raw PNG files"
TRANSCRIPT_DIR = CHAPTER_REPO / "Data/Transcripts"
NAMING_CSV = CHAPTER_REPO / "Data/Raw/Naming_CodesDONOT_TRASH.csv"
TEMPLATE_PATH = PAPER_REPO / "Templates/P00-G00-S0 PK-WAP TEMPLATE.md"
OUTPUT_DIR = CHAPTER_REPO / "Analysis/anchor_memos_vision_comparison"


def load_naming_mapping() -> Dict[str, str]:
    """Load the P-code to folder name mapping from CSV."""
    mapping = {}
    if NAMING_CSV.exists():
        with open(NAMING_CSV, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    name = row[0].strip().replace("\\_", "_")
                    code = row[1].strip()
                    mapping[code] = name
    return mapping


def find_png_folder(case_id: str, naming_map: Dict[str, str]) -> Optional[Path]:
    """
    Find the PNG folder for a given case ID.
    
    The folder naming is like "Group 1, Section 4, Huang Yuran"
    The case_id is like "P93-G1-S4"
    The naming_map entry is like "Yuan_KuangdiG1S4" -> "P93-G1-S4"
    """
    # Parse case_id
    parts = case_id.split("-")
    if len(parts) < 3:
        return None
    
    p_code = parts[0]  # P93
    group = parts[1].replace("G", "").replace("X", "")  # 1 or empty
    section = parts[2].replace("S", "").replace("X", "")  # 4 or empty
    
    # Get the name from mapping
    name_entry = naming_map.get(case_id, "")
    
    if not name_entry:
        return None
    
    # Extract name parts from entry like "Yuan_KuangdiG1S4" or "Yuran_G1S4" or "Zhao_HoganG_S_"
    # Remove the G##S## suffix (including G_S_ variants)
    import re
    # Remove patterns like G1S4, G_S_, G10S5, etc.
    name_part = re.sub(r'_?G\d*_?S\d*_?$', '', name_entry).strip("_")
    # Replace underscores with spaces
    name_part = name_part.replace("_", " ")
    
    print(f"  Looking for name '{name_part}' in Group {group}, Section {section}")
    
    # Search for matching folder
    if PNG_DIR.exists():
        for folder in PNG_DIR.iterdir():
            if folder.is_dir():
                folder_name = folder.name
                # Check if group/section match
                group_match = f"Group {group}," in folder_name if group else "Group Unknown" in folder_name
                section_match = f"Section {section}," in folder_name if section else "Section Unknown" in folder_name
                
                if group_match and section_match:
                    # Check name (partial match - any word from name_part)
                    name_words = name_part.lower().split()
                    folder_lower = folder_name.lower()
                    if any(word in folder_lower for word in name_words):
                        return folder
    
    return None


def encode_image_base64(image_path: Path) -> str:
    """Encode image to base64 for API."""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')


def load_png_images(png_folder: Path, max_images: int = 10) -> List[Dict]:
    """Load PNG images from folder, return list of image content dicts."""
    images = []
    png_files = sorted(png_folder.glob("*.png"))[:max_images]
    
    for png_file in png_files:
        base64_image = encode_image_base64(png_file)
        images.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{base64_image}",
                "detail": "high"
            }
        })
    
    return images


def find_transcript(case_id: str) -> Optional[Path]:
    """Find the transcript file for a case - handles S6 vs SX naming convention."""
    # Extract P-number for flexible matching
    p_num = case_id.split('-')[0]  # e.g., "P119"
    
    # First try exact match
    for ext in ['.txt', '.docx']:
        path = TRANSCRIPT_DIR / f"{case_id}{ext}"
        if path.exists():
            return path
    
    # For GX-SX cases, try with S6 instead
    if '-SX' in case_id:
        alt_id = case_id.replace('-SX', '-S6')
        for ext in ['.txt', '.docx']:
            path = TRANSCRIPT_DIR / f"{alt_id}{ext}"
            if path.exists():
                return path
    
    # For GX-SX cases with section X, try G#-S# variations  
    if '-GX-' in case_id:
        # Try P##-GX-S6
        alt_id = case_id.replace('-GX-SX', '-GX-S6')
        for ext in ['.txt', '.docx']:
            path = TRANSCRIPT_DIR / f"{alt_id}{ext}"
            if path.exists():
                return path
    
    # Finally, do a prefix search (P## prefix)
    for f in TRANSCRIPT_DIR.iterdir():
        if f.name.startswith(f"{p_num}-") and not "conflicted" in f.name.lower():
            if f.suffix.lower() in ['.txt', '.docx']:
                return f
    
    return None


def read_file(path: Path) -> str:
    """Read text or docx file."""
    if path.suffix.lower() == '.docx':
        try:
            from docx import Document
            doc = Document(path)
            return '\n'.join(para.text for para in doc.paragraphs)
        except ImportError:
            print("Warning: python-docx not installed")
            return path.read_text(encoding="utf-8", errors="ignore")
    return path.read_text(encoding="utf-8", errors="ignore")


def load_template() -> str:
    """Load the PK-WAP template."""
    if TEMPLATE_PATH.exists():
        return read_file(TEMPLATE_PATH)
    raise FileNotFoundError(f"Template not found: {TEMPLATE_PATH}")


def build_vision_prompt(
    transcript: str, 
    template: str, 
    case_id: str,
    images: List[Dict]
) -> List[dict]:
    """Build prompt with both images and text."""
    
    system_message = {
        "role": "system",
        "content": (
            "You are an expert educational researcher specializing in mathematical cognition "
            "and the Pirie-Kieren framework for recursive understanding. You analyze student-AI "
            "dialogue transcripts with deep pedagogical insight.\n\n"
            "You have been given BOTH the original PNG scans of the dialogue AND the extracted "
            "text transcript. Use BOTH sources to inform your analysis:\n"
            "- The PNG scans may contain visual formatting, diagrams, equations, or context "
            "  that may not be fully captured in the text extraction.\n"
            "- The text transcript provides searchable, quotable content.\n"
            "- Cross-reference both to ensure accuracy in your analysis.\n\n"
            "CRITICAL: Code PK layers CONSERVATIVELY. Most dialogues reach Property-Noticing "
            "or Formalising at most. Outer layers (Observing, Structuring, Inventising) are "
            "genuinely rare. When in doubt, code LOWER."
        )
    }
    
    # Build content with images first, then text
    content = [
        {
            "type": "text",
            "text": f"""I'm researching student–AI mathematical dialogue. Please analyze this transcript ({case_id}) using the Pirie–Kieren Work Analysis Protocol (PK-WAP).

Below are the ORIGINAL PNG SCANS of the dialogue, followed by the EXTRACTED TEXT.

Please examine both carefully and generate a Deep Research–style memo following the template structure exactly.

PNG SCANS ({len(images)} pages):
"""
        }
    ]
    
    # Add images
    content.extend(images)
    
    # Add text transcript
    content.append({
        "type": "text",
        "text": f"""

---
EXTRACTED TEXT TRANSCRIPT ({case_id}):
---

{transcript}

---
TEMPLATE (follow this structure exactly):
---

{template}

---

Generate the complete PK-WAP memo now. Note any discrepancies you observe between the PNG scans and extracted text.
"""
    })
    
    user_message = {
        "role": "user",
        "content": content
    }
    
    return [system_message, user_message]


def call_openrouter_vision(
    messages: List[dict],
    model: str = DEFAULT_MODEL,
    temperature: float = DEFAULT_TEMPERATURE,
    max_tokens: int = DEFAULT_MAX_TOKENS
) -> str:
    """Call OpenRouter API with vision support."""
    
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in environment")
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    
    print(f"  Calling OpenRouter Vision API ({model}, temp={temperature})...")
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )
    
    return response.choices[0].message.content.strip()


def analyze_case_with_vision(case_id: str, dry_run: bool = False) -> dict:
    """
    Analyze a case using both PNG images and text.
    
    Returns dict with analysis results and metadata.
    """
    print(f"\n{'='*60}")
    print(f"Vision Analysis: {case_id}")
    print(f"{'='*60}")
    
    # Load naming mapping
    naming_map = load_naming_mapping()
    print(f"  Loaded {len(naming_map)} case-to-name mappings")
    
    # Find PNG folder
    png_folder = find_png_folder(case_id, naming_map)
    if not png_folder:
        return {"status": "error", "message": f"PNG folder not found for {case_id}"}
    print(f"  Found PNG folder: {png_folder.name}")
    
    # Count PNGs
    png_files = list(png_folder.glob("*.png"))
    print(f"  Found {len(png_files)} PNG files")
    
    # Find transcript
    transcript_path = find_transcript(case_id)
    if not transcript_path:
        return {"status": "error", "message": f"Transcript not found for {case_id}"}
    print(f"  Found transcript: {transcript_path.name}")
    
    # Load template
    template = load_template()
    print(f"  Loaded PK-WAP template")
    
    if dry_run:
        print("\n  [DRY RUN - would send to API]")
        return {
            "status": "dry_run",
            "case_id": case_id,
            "png_folder": str(png_folder),
            "png_count": len(png_files),
            "transcript_path": str(transcript_path)
        }
    
    # Load content
    print(f"  Loading PNG images...")
    images = load_png_images(png_folder)
    
    print(f"  Loading transcript text...")
    transcript = read_file(transcript_path)
    
    # Build prompt
    messages = build_vision_prompt(transcript, template, case_id, images)
    
    # Call API
    start_time = time.time()
    memo_content = call_openrouter_vision(messages)
    elapsed = time.time() - start_time
    
    # Save output
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / f"{case_id}_PK-WAP_vision.md"
    output_file.write_text(memo_content, encoding="utf-8")
    
    print(f"\n  ✓ Complete in {elapsed:.1f}s")
    print(f"  Saved to: {output_file}")
    
    return {
        "status": "success",
        "case_id": case_id,
        "output_file": str(output_file),
        "elapsed_seconds": elapsed,
        "memo_length": len(memo_content),
        "png_count": len(png_files)
    }


def compare_memos(case_id: str):
    """Compare text-only vs vision memo for a case."""
    text_memo_path = CHAPTER_REPO / f"Analysis/anchor_memos_conservative/{case_id}_PK-WAP.md"
    vision_memo_path = OUTPUT_DIR / f"{case_id}_PK-WAP_vision.md"
    
    print(f"\n{'='*60}")
    print(f"Comparison: {case_id}")
    print(f"{'='*60}")
    
    if not text_memo_path.exists():
        print(f"  Text-only memo not found: {text_memo_path}")
        return
    
    if not vision_memo_path.exists():
        print(f"  Vision memo not found: {vision_memo_path}")
        return
    
    text_memo = text_memo_path.read_text()
    vision_memo = vision_memo_path.read_text()
    
    print(f"\n  Text-only memo: {len(text_memo)} chars")
    print(f"  Vision memo: {len(vision_memo)} chars")
    
    # Simple comparison - could be made more sophisticated
    print(f"\n  Key differences to check manually:")
    print(f"  1. Word count tables")
    print(f"  2. PK layer coding")
    print(f"  3. Evidence quotes")
    print(f"  4. Layer progression")
    
    return {
        "text_memo_chars": len(text_memo),
        "vision_memo_chars": len(vision_memo)
    }


def main():
    parser = argparse.ArgumentParser(
        description="PK-WAP Vision Analyzer - Compare text-only vs image+text analysis"
    )
    parser.add_argument(
        "--case", 
        type=str,
        help="Case ID to analyze (e.g., P93-G1-S4)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Test file discovery without API calls"
    )
    parser.add_argument(
        "--compare",
        action="store_true", 
        help="Compare text-only vs vision memos after generation"
    )
    parser.add_argument(
        "--list-available",
        action="store_true",
        help="List cases with both PNG and transcript available"
    )
    
    args = parser.parse_args()
    
    if args.list_available:
        print("Cases with both PNG folders and transcripts:\n")
        naming_map = load_naming_mapping()
        for code in sorted(naming_map.keys()):
            png_folder = find_png_folder(code, naming_map)
            transcript = find_transcript(code)
            if png_folder and transcript:
                png_count = len(list(png_folder.glob("*.png")))
                print(f"  {code}: {png_count} PNGs, {transcript.name}")
        return
    
    if args.case:
        result = analyze_case_with_vision(args.case, dry_run=args.dry_run)
        print(f"\nResult: {json.dumps(result, indent=2)}")
        
        if args.compare and result.get("status") == "success":
            compare_memos(args.case)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
