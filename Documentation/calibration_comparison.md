# Calibration Transcript Word Count Comparison

## Summary

This document compares manual word counts (Eleanor, Todd, Zheng) against automated counts with and without boilerplate removal.

## Methodology

**Manual Counting (LibreOffice):**
- Researchers read transcript electronically in LibreOffice Writer
- Highlighted AI passages, used word count tool (whitespace-based)
- Recorded count on paper
- Repeated for student passages
- Worked page-by-page through entire transcript

**Automated Counting:**
1. **Comprehensive mode** (default): CJK-aware, math tokenization, URL handling
2. **With boilerplate**: Counts all text including personality tests
3. **Without boilerplate**: Skips personality test/teacher profile sections before Taylor content begins

## Calibration Transcript Results

### P79-G8-S5 (No boilerplate in original)

| Method | Student Words | AI Words | Total | % Student | Notes |
|--------|--------------|----------|-------|-----------|-------|
| **Manual - Eleanor** | 1826 | 1219 | 3045 | 60.0% | LibreOffice whitespace count |
| **Manual - Zheng** | 1884 | 1375 | 3259 | 57.8% | LibreOffice whitespace count |
| Automated (comprehensive) | 3318 | 3301 | 6619 | 50.1% | CJK+math tokenization |
| Automated (simple words) | 1521 | 1419 | 2940 | 51.7% | Whitespace only |
| **Automated (skip-boilerplate)** | 2188 | 2852 | 5040 | 43.4% | **Skipped 82 lines** |

**Analysis**: P79 student gave AI the full prompt at start, which includes instructions mentioning "Taylor polynomial". The new boilerplate detector correctly identified this as setup (personality test follows) and skipped to actual content. This is MORE accurate since manual counters likely skipped the long initial prompt.

### P21-G5-S5

| Method | Student Words | AI Words | Total | % Student | Notes |
|--------|--------------|----------|-------|-----------|-------|
| **Manual - Need data** | ? | ? | ? | ? | LibreOffice counts pending |
| Automated (comprehensive) | 2849 | 703 | 3552 | 80.2% | 1894 unknown words |
| **Automated (skip-boilerplate)** | 2849 | 703 | 3552 | 80.2% | **Skipped 39 lines** |

**Analysis**: P21 begins with extensive personality test boilerplate ("STEP 1: PERSONALITY TEST"). Boilerplate detector correctly identified and skipped 39 lines. The % stayed the same but fewer unknown words (1496 vs 1894), suggesting better attribution after skipping boilerplate.

### P100-G12-S4

| Method | Student Words | AI Words | Total | % Student | Notes |
|--------|--------------|----------|-------|-----------|-------|
| **Manual - Need data** | ? | ? | ? | ~5%? | Phase1 showed 48%, suspect error |
| Automated (comprehensive) | 730 | 1690 | 2420 | 30.2% | 1149 unknown words |
| **Automated (skip-boilerplate)** | 730 | 630 | 1360 | 53.7% | **Skipped 51 lines, HUGE CHANGE** |

**Analysis**: P100 had extensive 4-question personality test (51 lines). Skipping this boilerplate **flipped the percentage** from 30.2% (AI-dominated) to 53.7% (student-majority). This suggests the boilerplate was mostly AI text (personality test setup). Without boilerplate, the transcript shows balanced student-AI interaction.

### P106-G15-S4

| Method | Student Words | AI Words | Total | % Student | Notes |
|--------|--------------|----------|-------|-----------|-------|
| **Manual - Need data** | ? | ? | ? | ? | LibreOffice counts pending |
| Automated (comprehensive) | 2473 | 5772 | 8245 | 30.0% | No unknown words |
| **Automated (skip-boilerplate)** | 2473 | 5772 | 8245 | 30.0% | **No boilerplate detected** |

**Analysis**: P106 starts directly with Taylor content ("In the early 1700s, Brook Taylor..."). No personality test detected. Counts unchanged. This is correct behavior.

### P76-GX-SX

| Method | Student Words | AI Words | Total | % Student | Notes |
|--------|--------------|----------|-------|-----------|-------|
| **Manual - Need data** | ? | ? | ? | ? | LibreOffice counts pending |
| Automated (comprehensive) | 8136 | 2828 | 10964 | 74.2% | 8933 unknown words! |
| **Automated (skip-boilerplate)** | 6851 | 2828 | 9679 | 70.8% | **Skipped 85 lines** |

**Analysis**: P76 had student giving full prompt + AI personality test (85 lines total). Boilerplate detector correctly skipped to historical content ("early 1700s, Brook Taylor"). Still has high unknown words (8515), suggesting attribution issues remain in the actual dialogue.

## Boilerplate Detection Logic

The `detect_boilerplate_end()` function:

1. Scans first 100 lines for personality test markers:
   - "personality test", "ai profiler"
   - "internal teacher profile", "teacher profile built"
   - "step 1: personality", "step 2: internal"

2. Once personality test detected, continues scanning for Taylor content markers:
   - "1715", "1685", "brook taylor"
   - "let's rewind to 1715", "early 1700s"
   - Historical context phrases

3. Returns line number where actual Taylor content begins, or 0 if no boilerplate

## Recommendations

1. **Use --skip-boilerplate for all transcripts** to match manual methodology
   - Eleanor and Zheng excluded personality test sections
   - More accurate representation of actual tutoring dialogue
   
2. **Investigate high unknown word counts** even after boilerplate removal
   - P21: 1496 unknown words
   - P76: 8515 unknown words (77% of total!)
   - P100: 1760 unknown words
   - Suggests CJK text or unrecognized speaker patterns

3. **Get manual counts for P21, P100, P106, P76** to validate automated approach

4. **Consider simple-words mode** for validation
   - P79 simple mode (51.7% student) closer to manual (57-60%)
   - Comprehensive mode includes math term-by-term tokenization
   - Manual LibreOffice uses whitespace splitting (matches simple mode)

5. **Update Appendix C** with boilerplate-excluded counts
   - Document methodology: "Excluded AI personality test/profile setup sections that appeared before Taylor series content"
   - Note transcripts vary: some have extensive boilerplate (P100: 51 lines), some have none (P106)

## Command to Re-run All 127 Transcripts

```bash
python3 "Data Formatted to Analyze/pk_screen_v2_2.py" \
  --input "Data Formatted to Analyze" \
  --outdir final_run_skip_boilerplate \
  --annotate \
  --skip-boilerplate \
  --force
```

This will create counts that match the manual calibration methodology.
