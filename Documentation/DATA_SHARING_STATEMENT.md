# Data Sharing Statement

## What We Share

In the interest of transparency and reproducibility, we share:

### 1. Complete Analysis Pipeline
- All Python scripts used for transcript processing and word counting
- Validation scripts comparing manual vs automated counts
- Documented protocols for both Phase I (word counting) and Phase II (PK-WAP analysis)

### 2. Calibration Data (De-identified)
- **Five calibration transcripts** (P79-G8-S5, P21-G5-S5, P100-G12-S4, P106-GX-SX, P76-GX-SX)
  - These are the actual processed transcript files used for methods validation
  - Already de-identified with participant codes
  - Selected by course instructor for format diversity
  
- **Manual vs automated comparison** (`calibration_validation_data.csv`)
  - Word counts from 3 independent researchers (manual highlighting method)
  - Automated word counts (both simple and comprehensive modes)
  - Inter-rater agreement statistics
  - Demonstrates automated methods achieve within 10pp of manual counts

### 3. Aggregate Results
- **Complete quantitative data** for all 127 transcripts (`aggregate_results_all_127.csv`)
  - Transcript ID, word counts, %Student Talk, status flags
  - NO transcript content—only metrics
  - Enables verification of:
    - How 30 anchor cases were selected (10 high, 10 low, 10 noteworthy)
    - Distribution of student participation across corpus
    - Ranking and quartile assignments

## What We Don't Share

We do **NOT** share the remaining 122 raw student transcripts to protect participant privacy:
- Transcripts may contain personal information, identifiable writing styles, or cultural references
- Students consented to research analysis but not public data release
- Course was conducted in China where no formal IRB process was required, but we uphold ethical standards

## Reproducibility Without Full Data

Researchers can fully reproduce our methods:

1. **Verify our counting methodology** works correctly:
   - Download the 5 calibration transcripts
   - Run our scripts
   - Compare to our published validation data
   - Should get identical automated counts and within 10pp of manual counts

2. **Apply to their own data**:
   - Collect similar student-AI conversation transcripts
   - Use our scripts and protocols
   - Replicate our analytical approach

3. **Verify our sample selection and rankings**:
   - Review aggregate results for all 127 transcripts
   - Check quartile boundaries
   - Confirm how we selected 30 anchor cases for deep analysis

## Ethical Considerations

This data sharing plan balances:
- ✅ **Transparency**: Methods, code, and validation data fully open
- ✅ **Reproducibility**: Others can verify and replicate our approach  
- ✅ **Privacy**: Student data protected; only necessary validation samples shared
- ✅ **Utility**: Sufficient data for methodological verification and replication

## Repository Location

All shared materials available at:
**https://github.com/[username]/TEA-AI-Calculus-Research**

## Contact

Questions about data access or methodology:
[Your contact information]
