# Boilerplate Analysis for Calibration Transcripts

## Issue
Eleanor and Zheng manually counted transcripts by highlighting AI vs. Student text in LibreOffice. They likely **excluded** the initial AI-generated boilerplate (personality test, teacher profile setup) that appears before the actual Taylor series discussion begins.

Our automated script counts ALL text, including boilerplate, leading to discrepancies.

## Boilerplate Boundaries in Calibration Transcripts

### P79-G8-S5.txt (NO BOILERPLATE)
- **Lines 1-45**: Student gives AI the full prompt/instructions upfront
- **Line 35**: First mention of "Taylor polynomial"
- **Line 47+**: AI response begins actual Taylor content
- **Decision**: No boilerplate to exclude - student-initiated conversation

### P21-G5-S5.txt (HAS BOILERPLATE)
- **Lines 1-39**: AI personality test + teacher profile (BOILERPLATE)
  - "STEP 1: PERSONALITY TEST" (line 5)
  - "STEP 2: INTERNAL TEACHER PROFILE" (line 19)
  - Student response: "I prefer direct, concise explanations" (line 17)
- **Line 40+**: "Taylor polynomials (1685)" - ACTUAL CONTENT BEGINS
- **Decision**: Exclude lines 1-39 from word count

### P100-G12-S4.txt (HAS BOILERPLATE)
- **Lines 1-51**: AI personality test (4 questions) + teacher profile (BOILERPLATE)
  - "Step 1: Personality Test" (line 3)
  - Questions 1-4 (lines 9-47)
  - "Step 2: Internal Teacher Profile Built" (line 49)
- **Line 52+**: "Let's rewind to 1715. Brook Taylor..." - ACTUAL CONTENT BEGINS
- **Decision**: Exclude lines 1-51 from word count

### P106-G15-S4.txt (NO CLEAR BOILERPLATE)
- **Line 1**: Starts directly with "Al Teacher Profiler Guides Academic Challenge"
- **Lines 3-6**: Historical context about Brook Taylor (1700s)
- **Decision**: No clear boilerplate section - appears to be actual content from start
- **NOTE**: Student later pastes the full prompt (lines ~30-60), creating confusion

### P76-GX-SX.txt (HAS BOILERPLATE)
- **Lines 1-85**: Student gives full prompt, AI personality test begins (BOILERPLATE)
  - Line 4: "Me: You are a Personality-based Al Teacher Generator..."
  - Lines 7-85: AI conducts multi-question personality assessment
- **Line 86+**: "Let's dive into Taylor polynomials..." - ACTUAL CONTENT BEGINS
- **Decision**: Exclude lines 1-85 from word count

## Pattern Recognition

**Boilerplate indicators:**
1. "Personality Test" or "Personality-based Al Teacher Generator"
2. "STEP 1: PERSONALITY TEST" or "Step 1: Personality Test"
3. "INTERNAL TEACHER PROFILE" or "Teacher Profile Built"
4. "Temporary AI Profiler Introduction"
5. Questions about learning preferences, tone preferences, teaching style

**Content start indicators:**
1. First mention of "Taylor" (polynomial/series)
2. Historical context: "1715" or "1685" or "Brook Taylor"
3. "Let's dive into Taylor polynomials"
4. "Historical Context" section that discusses actual math topic

## Proposed Solution

Add a `--skip-boilerplate` flag to `pk_screen_v2_2.py` that:

1. Scans initial pages (0-2) for boilerplate keywords
2. Identifies line number where Taylor content begins
3. Excludes everything before that line from word counting
4. Logs the exclusion in output for transparency

## Methodology Justification

**Why exclude boilerplate:**
- Manual calibrators (Eleanor, Zheng, Todd) excluded it during highlighting
- Boilerplate is not part of the actual tutoring dialogue about Taylor series
- Including it inflates AI word counts and skews percentages
- Goal is to measure student-AI interaction during math learning, not personality profiling

**Documentation needed:**
- Update methods.tex to explain boilerplate exclusion
- Note that some transcripts (P79, P106) have minimal/no boilerplate
- Specify that calibration counts excluded boilerplate sections
