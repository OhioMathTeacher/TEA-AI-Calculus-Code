WORD COUNTING VALIDATION - FINDINGS
=====================================

Date: 2025-11-29
Files Tested: P79-G8-S5, P100-G12-S4, P21-G5-S5

## KEY FINDING: Inconsistent Transcript Formats

### P79-G8-S5 (Actual Conversation Transcript)
- Format: Turn-by-turn with explicit speaker markers (P: / D:)
- Manual counts (within tolerance):
  - Eleanor: 60.0% student (1826/1219/3045)
  - Zheng:   57.8% student (1884/1375/3259)
- Automated annotation: **REVERSED speaker attribution**
  - Original tags: 43.5% student (WRONG)
  - Flipped tags:  56.5% student (CORRECT - within 2.4pp of manual avg)

### P100-G12-S4 (AI Instructions Document)
- Format: Mostly AI's script/instructions with minimal student input
- Manual count:
  - Zheng: 4.0% student (68/1617/1685)
- Automated annotation: Correct speaker attribution (mostly [AI] tags)
  - Original count: 4.5% student (84/1798/1882) - CLOSE to manual
  
### P21-G5-S5 (Unknown - file is 0 bytes in annotations)
- Annotated file is empty
- Manual count:
  - Zheng: 15.8% student (377/2006/2383)
- Cannot validate

## ROOT CAUSES

1. **Inconsistent Transcript Formats**
   - Some files are actual conversations (P79: "P:" and "D:" markers)
   - Some files are AI instruction documents (P100: mostly AI prompts)
   - Annotation script handles these differently

2. **Speaker Attribution Reversal**
   - For conversation transcripts like P79, automated tagging reversed AI/Student
   - This may be due to misinterpreting who initiated the conversation
   
3. **Annotation Failures**
   - P21 produced a 0-byte annotated file
   - Many files marked "needs_review" with high "unknown" word counts

## COMPREHENSIVE WORD COUNTING TOKENIZATION

The pk_screen_v2_2.py tokenization logic is CORRECT and matches Appendix B rules:

✓ URLs/emails count as 1 token each
✓ CJK text counted as ceil(length/2)
✓ Math expressions tokenized (each operator/variable = 1 token)
✓ AI preambles removed
✓ Punctuation-only tokens ignored

**Validated on P79 with flipped tags:**
- Automated: 56.5% student (1821/1401/3222)  
- Manual avg: 58.9% student
- Difference: 2.4 percentage points (WITHIN 10% tolerance)

## RECOMMENDED SOLUTION

### Option 1: Fix Automated Annotation (Complex)
- Review why P79 got reversed attribution
- Fix annotation script to handle different transcript formats
- Re-annotate all 127 transcripts
- Validate against manual calibration
- Re-run counting on fixed annotations

### Option 2: Manual Attribution + Automated Counting (Hybrid)
- Use original transcript files with existing speaker markers (P:, D:, etc.)
- Manually verify/add speaker markers for files without them
- Run tokenization directly on marked-up originals
- Skip the annotation step entirely

### Option 3: Use Original Phase 1 Data (Pragmatic)
- Accept that phase1_wordcount_summaryKEEPTHIS.csv came from SOME counting method
- It's already in Appendix C Table 5
- Focus on completing the 30 PK-WAP analyses instead of re-counting
- Document limitations in paper

## NEXT STEPS

1. **IMMEDIATE:** Determine which transcript files need speaker attribution fixes
   - Check all 127 files for format consistency
   - Identify files with clear P:/D: markers vs. those without

2. **VALIDATE:** Run comprehensive test on all 5 manual calibration files
   - P79-G8-S5 (tested - works with flipped tags)
   - P21-G5-S5 (annotated file empty - need to re-annotate)
   - P100-G12-S4 (tested - works with original tags)
   - P106-GX-SX (not yet tested)
   - P76-GX-SX (not yet tested)

3. **DECIDE:** Choose Option 1, 2, or 3 based on:
   - Time available
   - Importance of precise word counts for research conclusions
   - Whether existing phase1 data is "close enough"

4. **EXECUTE:** Once validation complete and approach chosen:
   - Generate new counts for all 127 transcripts
   - Update Appendix C Table 5
   - Re-rank and potentially re-select 30 anchor cases
   - Begin/continue PK-WAP deep analyses

## FILES CREATED FOR VALIDATION

- validate_counting.py: Compare automated vs manual counts
- test_comprehensive_count.py: Test tokenization logic
- test_flipped_count.py: Test with reversed speaker tags
- reconcile_counts.py: Original comparison script
- WORD_COUNT_STATUS_REPORT.md: Initial findings
- REALITY_CHECK.md: Gap analysis of claimed vs actual work
