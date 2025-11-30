# TEA AI Calculus Research - Reproducibility Repository

This repository contains analysis scripts and protocols for the research paper:  
**"[Your Paper Title]: Examining Student-AI Interaction Through the Pirie-Kieren Framework"**

## Contents

### `/scripts/`
Python scripts for automated transcript analysis:
- `pk_screen_v2_2.py` - Main transcript screening and word counting pipeline
- `recount_from_annot.py` - Word count validation from annotated transcripts
- Supporting utilities for data processing

### `/protocols/`
Research protocols and documentation:
- `transcript_screening_protocol.md` - Phase I screening methodology
- `pk_wap_protocol.md` - Pirie-Kieren Work Analysis Protocol (Phase II)
- `calibration_methodology.md` - Inter-rater reliability calibration process

### `/validation/`
Validation and quality assurance scripts:
- `validate_counting.py` - Compare automated vs manual counts
- `test_calibration.py` - Verify counting against calibration data
- Calibration summary statistics (anonymized)

### `/data/`
Shareable research data (de-identified):
- `calibration_validation_data.csv` - Manual vs automated counts for 5 calibration transcripts
- `aggregate_results_all_127.csv` - Word count results for all 127 transcripts (transcript IDs only, no content)
- `calibration_transcripts/` - The 5 processed transcripts used for calibration (P79, P21, P100, P106, P76)

**Note**: These 5 transcripts are shared to enable full reproducibility verification. They are already de-identified with participant codes (P79, P21, etc.). The remaining 122 transcripts are not shared to protect participant privacy, but aggregate statistics for all 127 are provided.

## Reproducibility

### Manual Calibration
Three researchers independently counted five transcripts using LibreOffice's word count feature:
- **Method**: Page-by-page highlighting of AI vs Student text
- **Tool**: LibreOffice Writer (whitespace-based word splitting)
- **Inter-rater agreement**: Within 10 percentage points on %Student Talk
- **Transcripts**: P79-G8-S5, P21-G5-S5, P100-G12-S4, P106-GX-SX, P76-GX-SX

### Automated Pipeline
The `pk_screen_v2_2.py` script automates the calibrated methodology:

```bash
# Standard mode (comprehensive tokenization)
python3 pk_screen_v2_2.py --input transcripts/ --outdir results/ --annotate

# Simple mode (matches manual calibration)
python3 pk_screen_v2_2.py --input transcripts/ --outdir results/ --simple-words --annotate
```

**Key features:**
- Speaker attribution with explicit label detection (AI:, Student:, P:, D:, etc.)
- Instruction block removal (RB4 preambles)
- Math expression tokenization (term-by-term counting)
- CJK character handling (ceil(length/2) approximation)
- URL/email handling (single token each)

### Requirements

```
python >= 3.10
python-docx  # for .docx file support
joblib       # optional, for ML-based speaker classification
```

## Data Availability

### Shared Data (De-identified)

**1. Five Calibration Transcripts** (`data/calibration_transcripts/`)
- P79-G8-S5.txt, P21-G5-S5.txt, P100-G12-S4.txt, P106-GX-SX.txt, P76-GX-SX.txt
- These transcripts are shared to enable complete reproducibility verification
- Already de-identified with participant codes
- Selected for format diversity by course instructor

**2. Calibration Validation Data** (`data/calibration_validation_data.csv`)
- Manual word counts by 3 researchers (Eleanor, Todd, Zheng)
- Automated word counts (simple and comprehensive modes)
- Inter-rater agreement statistics
- Readers can verify that automated methods match manual calibration within 10pp tolerance

**3. Aggregate Results** (`data/aggregate_results_all_127.csv`)
- Word count statistics for all 127 transcripts
- Format: Transcript_ID, Student_Words, AI_Words, Total_Words, %_Student, Status
- No transcript content—only quantitative metrics
- Allows verification of:
  - Quartile rankings (for selecting 10 high, 10 low, 10 noteworthy cases)
  - Distribution of student participation
  - Selection criteria for 30 anchor cases

### How to Verify Reproducibility

```bash
# 1. Clone this repository
git clone https://github.com/[username]/TEA-AI-Calculus-Research
cd TEA-AI-Calculus-Research

# 2. Run the script on the 5 calibration transcripts
python3 scripts/pk_screen_v2_2.py \
    --input data/calibration_transcripts/ \
    --outdir my_verification/ \
    --simple-words \
    --annotate

# 3. Compare your results to the validation data
cat my_verification/summary.csv
cat data/calibration_validation_data.csv

# Your automated counts should match our automated counts exactly
# And should be within ~10pp of manual counts
```

### Privacy Protection

**Raw student transcripts (122 of 127) are NOT included** to protect participant privacy. Only the 5 calibration transcripts used for methods validation are shared, as they are necessary for reproducibility verification and are already de-identified.

## Citation

If you use these methods or scripts, please cite:

```bibtex
[Your citation will go here]
```

## License

Scripts: MIT License  
Protocols/Documentation: CC BY 4.0  
(See LICENSE file for details)

## Contact

Questions about methodology or replication: [contact info]
