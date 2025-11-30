# TEA AI Calculus Research - Code Repository

This repository contains the analysis code and protocols used in the study:

**"Generative AI as a Recursive Learning Partner: A Pirie-Kieren Analysis of Taylor Series Instruction in University Calculus"**

## Overview

This codebase operationalizes qualitative educational research using GenAI to systematically analyze student-AI dialogue transcripts through the Pirie-Kieren Work Analysis Protocol (PK-WAP).

## Repository Contents

### Scripts/

**Core Analysis Tools:**
- `pkwap_analyzer.py` - Main PK-WAP analysis engine using OpenAI API
- `process_anchor_cases.py` - Batch processing for anchor case selection
- `select_anchor_transcripts.py` - Transcript selection based on word count analysis
- `pk_screen_v2_2.py` - Phase I word count screening tool

**Validation & Calibration:**
- `validate_counting.py` - Word count validation against manual coding
- `reconcile_counts.py` - Cross-validation of counting methodologies
- `test_all_calibration.py` - Calibration testing suite

**Interactive Tools:**
- `transcript_reviewer.py` - Flask web app for systematic case tagging
- `review_candidates.py` - Noteworthy case candidate review interface
- `analyze_pkwap_memos.py` - Post-hoc memo analysis and aggregation

### Templates/

- `P00-G00-S0 PK-WAP TEMPLATE.md` - Gold standard template for PK-WAP memos
- `reviewer.html` - Web interface template for transcript review

### Documentation/

- Reproducibility guidelines
- Validation reports
- Calibration analyses
- Data sharing statements

## Key Features

### 1. Automated PK-WAP Analysis
The `pkwap_analyzer.py` script:
- Reads student-AI transcripts
- Applies Pirie-Kieren theoretical framework
- Generates structured analytic memos
- Identifies folding-back moments and layer progression
- Maintains consistency across large datasets (30+ cases)

### 2. Two-Phase Analysis Pipeline

**Phase I: Quantitative Screening**
- Automated word count analysis (`pk_screen_v2_2.py`)
- Student vs. AI talk percentage calculation
- Identification of high/low engagement cases

**Phase II: Qualitative Deep Analysis**
- PK-WAP coding via GenAI
- Evidence-based layer identification
- Recursive learning pattern detection

### 3. Quality Control
- Manual validation against expert coding
- Calibration testing across multiple coders
- Count reconciliation procedures

## Installation

```bash
# Clone the repository
git clone https://github.com/OhioMathTeacher/TEA-AI-Calculus-Code.git

# Install dependencies
pip install openai python-docx flask pandas

# Set your OpenAI API key
export OPENAI_API_KEY='your-key-here'
```

## Usage

### Running PK-WAP Analysis

```python
from pkwap_analyzer import analyze_transcript

# Analyze a single transcript
result = analyze_transcript('transcript.txt', 
                            template='Templates/P00-G00-S0 PK-WAP TEMPLATE.md')
```

### Phase I Screening

```python
from pk_screen_v2_2 import screen_transcripts

# Screen all transcripts for word counts
results = screen_transcripts(transcript_dir='transcripts/')
```

### Launching Transcript Reviewer

```bash
python Scripts/transcript_reviewer.py
# Navigate to http://localhost:5000
```

## Methodological Notes

### GenAI as Research Partner
This project demonstrates proof-of-concept for using GenAI as a systematic qualitative analysis partner. Key principles:

1. **Theory-Driven Prompting**: Analysis prompts embed Pirie-Kieren framework
2. **Template Enforcement**: Strict output formatting ensures consistency
3. **Human Oversight**: Manual review and calibration validate AI coding
4. **Transparency**: All prompts, templates, and protocols are documented

### Reproducibility
All analysis is logged and traceable:
- API interactions logged for reproducibility
- Template versions tracked
- Calibration data provided
- Validation procedures documented

## Citation

If you use this code, please cite:

```bibtex
[Citation details from CITATION.cff]
```

## Data Availability

**Note:** Student transcript data is not included in this repository due to privacy protections. The code is provided to demonstrate methodology and enable replication with similar datasets.

For questions about data access for verification purposes, contact the authors.

## License

[To be determined - recommend MIT or GPL for open science]

## Contact

For questions or collaboration: [Contact via repository issues]

---

**Companion Repository:** Full research materials (private) available to reviewers upon request.
