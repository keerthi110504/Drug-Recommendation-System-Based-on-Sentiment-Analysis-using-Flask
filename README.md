# MediSense — Drug Recommendation System

## Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the app
```bash
python app.py
```

### 3. Open in browser
Navigate to: http://127.0.0.1:5000

---

## What was fixed

### Bug: "very bad" was classified as Positive

**Root cause:** The original sentiment engine scored the word "bad" as negative,
but the intensifier "very" was handled separately and added a positive boost
that outweighed the "bad" score.

**Fix (three-layer approach in `app.py`):**

1. **Phrase overrides** — checked *first*. Patterns like `very bad`, `very poor`,
   `not helpful`, `would not recommend` are matched as complete phrases and
   assigned a strong negative score before any word-level processing.

2. **Negation detection** — words like `not`, `never`, `don't`, `didn't` flip
   the polarity of the next sentiment word in the sentence.

3. **Word-level scoring** — individual positive/negative words are scored, but
   words already captured by phrase overrides are skipped to avoid double-counting.

**Test cases (all now correct):**
| Input            | Expected  | Result    |
|------------------|-----------|-----------|
| very bad         | Negative  | ✅ Negative |
| very good        | Positive  | ✅ Positive |
| not helpful      | Negative  | ✅ Negative |
| great medication | Positive  | ✅ Positive |
| terrible side effects | Negative | ✅ Negative |

---

## Project Structure
```
medisense/
├── app.py              # Flask app + sentiment engine (FIXED)
├── requirements.txt
├── templates/
│   ├── index.html
│   └── about.html
└── static/
    ├── css/style.css
    └── js/app.js
```
