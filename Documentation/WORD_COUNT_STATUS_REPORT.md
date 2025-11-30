# Word Count Status Report
**Date:** November 29, 2025  
**Created by:** GitHub Copilot assisting Todd

## Current Situation

### What You Have:
1. **Manual counts** for 5 transcripts (P01-P05) done by Zheng, Eleanor, and Todd
   - Used LibreOffice Writer's word count tool
   - Achieved inter-rater agreement within 10% tolerance
   - Established rules for counting (math expressions as 1 word, etc.)

2. **Automated counts in Appendix C** from `phase1_wordcount_summaryKEEPTHIS.csv`
   - Contains all 127 transcripts
   - Currently displayed in Manuscript (LaTeX)/appendix.tex Table 5
   - Source/method of generation: **UNKNOWN** - needs investigation

3. **Multiple Python scripts** for word counting:
   - `pk_screen_v2_2.py` - Most recent version, attempts speaker attribution
   - `recount_from_annot.py` - Counts from pre-annotated files
   - Various runs in different folders (screen_run_final, out_rows-run3, etc.)

4. **Annotated transcripts** in multiple locations:
   - `python_word_counts/annotated/` - Has [AI]/[Student] labels
   - `out_rows-run3/annotations/` - Also has labels
   - Quality/consistency: **NEEDS VERIFICATION**

### The Problem:
Different counting methods produce very different results:

| Method | Source | Match with Appendix C |
|--------|--------|---------------------|
| Manual (5 files) | You + Zheng + Eleanor | ✓ Presumed to match |
| phase1_wordcount_summaryKEEPTHIS.csv | Unknown | ✓ This IS Appendix C |
| screen_run_final | pk_screen_v2_2.py | ✗ Very different (flipped AI/Student in many cases) |
| summary_recounted.csv | recount_from_annot.py on python_word_counts | ✗ Different from phase1 |

**Example discrepancy (P01-G8-S4):**
- Appendix C (phase1): 14.3% student (112 student, 671 AI)
- Recounted: 7.1% student (38 student, 494 AI)
- screen_run_final: 73.7% student (3114 student, 1111 AI) 🚩 REVERSED!

## Root Cause Analysis

The speaker attribution is failing in different ways:

1. **screen_run_final** appears to be mis-labeling AI instructions as Student text (inverted)
2. **annotated files** may have different annotation standards or were created by different processes
3. **phase1 data** origin is unclear - may have been manually corrected or from a different annotation run

## Questions That Need Answers

1. **Where did `phase1_wordcount_summaryKEEPTHIS.csv` come from?**
   - Was it manually created/corrected?
   - Which annotation run produced it?
   - Can we reproduce it?

2. **Which annotated transcripts are "correct"?**
   - python_word_counts/annotated/?
   - out_rows-run3/annotations/?
   - Are there hand-corrected versions?

3. **What was the inter-rater reliability process?**
   - Which 5 transcripts did you count manually?
   - What were the exact counts for those 5?
   - Can we validate against phase1 data?

## Recommended Next Steps

### OPTION A: Trust and Document phase1 data
If `phase1_wordcount_summaryKEEPTHIS.csv` is already verified:
1. Document its origin in the paper
2. Use it as-is for Appendix C (already done)
3. Use it to select anchor transcripts for PK analysis
4. Move to Phase II analysis

### OPTION B: Verify and potentially re-count
If you need to regenerate/verify the counts:
1. Locate the 5 manually counted transcripts
2. Compare manual counts to phase1 data for those 5
3. If they match → phase1 is good
4. If they don't → need to find the source or re-annotate

### OPTION C: Fresh start with verified annotation
If annotations are unreliable:
1. Select a subset (maybe 30 anchor cases)
2. Manually verify/correct [AI]/[Student] labels
3. Use recount_from_annot.py on verified files
4. Extrapolate/validate for remaining transcripts

## What I Recommend Doing TODAY

1. **Find the manual count data for the 5 transcripts** (P01-P05?)
   - Check if you have a spreadsheet or notes from that process
   - Compare to phase1 to see if they match

2. **If manual counts match phase1:**
   - Accept phase1 as ground truth
   - Document the methodology in methods.tex
   - Proceed to select anchor transcripts

3. **If manual counts don't match or can't be found:**
   - Pick 3-5 transcripts to manually verify RIGHT NOW
   - Use those to validate which automated method is closest
   - Decide on path forward

## Files to Check
- [ ] Any spreadsheets from July/August with manual counts
- [ ] Email threads with Zheng/Eleanor about the 5 transcripts
- [ ] Notes about which transcripts were P01-P05
- [ ] Any "gold standard" or "verified" folders

## Current Data Files

### Counts:
- `Analyzed Cases (Phase 1 and 2)/phase1_wordcount_summaryKEEPTHIS.csv` ← Currently in Appendix C
- `Data Formatted to Analyze/screen_run_final/summary.csv` ← From pk_screen_v2_2.py
- `Data Formatted to Analyze/python_word_counts/summary_recounted.csv` ← Just generated

### Annotations:
- `Data Formatted to Analyze/python_word_counts/annotated/*.txt`
- `Data Formatted to Analyze/out_rows-run3/annotations/*.txt`

### Scripts:
- `Data Formatted to Analyze/pk_screen_v2_2.py` ← Latest screening script
- `Data Formatted to Analyze/recount_from_annot.py` ← Recounting from annotations
