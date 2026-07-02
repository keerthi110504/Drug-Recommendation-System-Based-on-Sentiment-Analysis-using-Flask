from flask import Flask, render_template, request, jsonify
import json
import re
from collections import Counter
from dataset import REVIEWS

app = Flask(__name__)

# ── Improved Sentiment Analysis ───────────────────────────────────────────────

# Negation words that flip sentiment
NEGATIONS = {"not", "no", "never", "neither", "nor", "barely", "hardly",
             "scarcely", "without", "don't", "doesn't", "didn't", "isn't",
             "wasn't", "aren't", "weren't", "won't", "wouldn't", "can't",
             "couldn't", "shouldn't", "very bad", "very poor", "very terrible"}

POSITIVE_WORDS = {
    "good": 1.0, "great": 1.5, "excellent": 1.5, "amazing": 1.5,
    "wonderful": 1.5, "fantastic": 1.5, "outstanding": 1.5, "superb": 1.5,
    "best": 1.5, "perfect": 1.5, "love": 1.2, "loved": 1.2, "like": 0.5,
    "helpful": 1.0, "effective": 1.0, "recommend": 1.0, "recommended": 1.0,
    "better": 0.8, "improved": 1.0, "improvement": 1.0, "works": 0.7,
    "worked": 0.7, "working": 0.7, "relief": 1.2, "relieved": 1.2,
    "comfortable": 0.8, "happy": 1.0, "pleased": 1.0, "satisfied": 1.0,
    "positive": 0.8, "easy": 0.6, "safe": 0.6, "mild": 0.3, "okay": 0.3,
    "ok": 0.3, "fine": 0.3, "nice": 0.7, "useful": 0.8, "clear": 0.5,
    "cleared": 0.8, "lifesaver": 1.5, "changin": 1.0, "changing": 1.0,
    "worth": 0.8, "manageable": 0.5, "stable": 0.6, "controlled": 0.6,
    "win": 1.0, "tolerable": 0.3, "decent": 0.5,
}

NEGATIVE_WORDS = {
    "bad": -1.0, "terrible": -1.5, "awful": -1.5, "horrible": -1.5,
    "dreadful": -1.5, "poor": -1.0, "worse": -1.0, "worst": -1.5,
    "hate": -1.5, "hated": -1.5, "dislike": -1.0, "useless": -1.2,
    "ineffective": -1.2, "dangerous": -1.3, "harmful": -1.3, "side": -0.3,
    "effects": -0.2, "nausea": -0.8, "pain": -0.8, "painful": -1.0,
    "dizziness": -0.8, "dizzy": -0.8, "uncomfortable": -0.8,
    "inconsistent": -0.6, "slow": -0.4, "swelling": -0.5, "cough": -0.5,
    "rash": -0.7, "severe": -0.8, "anxiety": -0.5, "insomnia": -0.7,
    "sweating": -0.5, "dependency": -0.8, "habit": -0.6, "forming": -0.5,
    "risk": -0.4, "struggle": -0.8, "struggled": -0.8, "negative": -0.8,
    "problem": -0.8, "problems": -0.8, "difficult": -0.7, "hard": -0.4,
    "failure": -1.2, "failed": -1.2, "fail": -1.2, "wrong": -0.8,
    "mistake": -0.8, "regret": -1.0, "disappointed": -1.0,
    "disappointing": -1.0, "frustrated": -0.9, "frustrating": -0.9,
    "annoying": -0.6, "annoy": -0.6, "irritating": -0.6, "nasty": -1.0,
    "dryness": -0.5, "dry": -0.3, "purging": -0.5, "nausea": -0.7,
    "uti": -0.6, "cautiously": -0.4, "caution": -0.4,
}

# High-confidence phrase overrides (checked BEFORE word-level scoring)
PHRASE_OVERRIDES = [
    # Negative phrases
    (r"\bvery bad\b",           -2.0),
    (r"\bvery poor\b",          -2.0),
    (r"\bvery terrible\b",      -2.5),
    (r"\bvery awful\b",         -2.5),
    (r"\bextremely bad\b",      -2.5),
    (r"\breally bad\b",         -1.8),
    (r"\bso bad\b",             -1.8),
    (r"\bquite bad\b",          -1.5),
    (r"\bpretty bad\b",         -1.5),
    (r"\bworst ever\b",         -2.5),
    (r"\btotal failure\b",      -2.5),
    (r"\bnot good\b",           -1.2),
    (r"\bnot helpful\b",        -1.2),
    (r"\bnot effective\b",      -1.2),
    (r"\bnot recommend\b",      -1.5),
    (r"\bdon'?t recommend\b",   -1.5),
    (r"\bwould not recommend\b",-1.8),
    (r"\bmade.*worse\b",        -1.5),
    (r"\bside effects\b",       -0.5),
    # Positive phrases
    (r"\bvery good\b",           2.0),
    (r"\bvery great\b",          2.0),
    (r"\bvery effective\b",      1.8),
    (r"\bvery helpful\b",        1.8),
    (r"\bvery happy\b",          1.8),
    (r"\breally good\b",         1.8),
    (r"\bhighly recommend\b",    2.0),
    (r"\blife changing\b",       2.0),
    (r"\blife-changing\b",       2.0),
    (r"\blifesaver\b",           2.0),
    (r"\bwould definitely recommend\b", 2.0),
]

def analyze_sentiment(text: str) -> dict:
    """
    Improved rule-based sentiment analyser.
    Returns: {label, confidence, positive, neutral, negative}
    """
    text_lower = text.lower().strip()

    if not text_lower:
        return {"label": "Neutral", "confidence": 1.0,
                "positive": 0.33, "neutral": 0.34, "negative": 0.33}

    score = 0.0

    # 1. Phrase-level overrides (highest priority)
    matched_phrases = set()
    for pattern, weight in PHRASE_OVERRIDES:
        if re.search(pattern, text_lower):
            score += weight
            # Track which individual words are already covered
            for word in re.findall(r'\b\w+\b', pattern.replace(r'\b','').replace('?','').replace('.*','')):
                matched_phrases.add(word)

    # 2. Word-level scoring with simple negation window
    words = re.findall(r"\b\w+(?:'\w+)?\b", text_lower)
    i = 0
    while i < len(words):
        word = words[i]

        # Check if this word is a negation; if so, flip next sentiment word
        if word in NEGATIONS:
            # Look ahead up to 3 words for a sentiment word
            for j in range(i + 1, min(i + 4, len(words))):
                nw = words[j]
                if nw in POSITIVE_WORDS and nw not in matched_phrases:
                    score += POSITIVE_WORDS[nw] * -1.2  # flip & amplify
                    matched_phrases.add(nw)
                    break
                if nw in NEGATIVE_WORDS and nw not in matched_phrases:
                    score += NEGATIVE_WORDS[nw] * -0.8  # double-negative = mild positive
                    matched_phrases.add(nw)
                    break
            i += 1
            continue

        if word in matched_phrases:
            i += 1
            continue

        if word in POSITIVE_WORDS:
            score += POSITIVE_WORDS[word]
        elif word in NEGATIVE_WORDS:
            score += NEGATIVE_WORDS[word]

        i += 1

    # 3. Intensifier boost ("very", "extremely", "really" before sentiment words)
    intensifiers = {"very": 1.5, "extremely": 1.8, "really": 1.4,
                    "so": 1.3, "quite": 1.2, "pretty": 1.1, "absolutely": 1.7}
    for idx, word in enumerate(words[:-1]):
        if word in intensifiers:
            next_word = words[idx + 1]
            if next_word in POSITIVE_WORDS or next_word in NEGATIVE_WORDS:
                # Already handled in phrase overrides; just a safety boost
                pass  # phrase overrides cover the common "very bad" cases

    # 4. Convert score → probabilities
    # Clamp score to [-5, 5] range then sigmoid-style mapping
    score = max(-5.0, min(5.0, score))

    if score > 0.3:
        label = "Positive"
        pos  = min(0.95, 0.5 + score * 0.09)
        neg  = max(0.02, 0.25 - score * 0.04)
        neu  = max(0.03, 1.0 - pos - neg)
    elif score < -0.3:
        label = "Negative"
        neg  = min(0.95, 0.5 + abs(score) * 0.09)
        pos  = max(0.02, 0.25 - abs(score) * 0.04)
        neu  = max(0.03, 1.0 - pos - neg)
    else:
        label = "Neutral"
        neu  = 0.60
        pos  = 0.20
        neg  = 0.20

    # Normalise so they sum to 1
    total = pos + neu + neg
    pos  = round(pos / total, 3)
    neu  = round(neu / total, 3)
    neg  = round(1 - pos - neu, 3)

    confidence = pos if label == "Positive" else (neg if label == "Negative" else neu)

    return {
        "label":      label,
        "confidence": round(confidence, 3),
        "positive":   pos,
        "neutral":    neu,
        "negative":   neg,
    }


def get_condition_stats(condition: str):
    cond_reviews = [r for r in REVIEWS if r["condition"].lower() == condition.lower()]
    if not cond_reviews:
        return None
    ratings = [r["rating"] for r in cond_reviews]
    sentiments = [analyze_sentiment(r["review"])["label"] for r in cond_reviews]
    cnt = Counter(sentiments)
    total = len(cond_reviews)
    distribution = Counter(r["rating"] for r in cond_reviews)
    return {
        "total":        total,
        "avg_rating":   round(sum(ratings) / total, 2),
        "positive_pct": round(cnt["Positive"] / total * 100, 1),
        "negative_pct": round(cnt["Negative"] / total * 100, 1),
        "distribution": {str(i): distribution.get(i, 0) for i in range(1, 11)},
        "recent":       cond_reviews[:3],
    }


def get_recommendations(condition: str, symptom_text: str):
    cond_reviews = [r for r in REVIEWS if r["condition"].lower() == condition.lower()]
    if not cond_reviews:
        return []
    sym_sentiment = analyze_sentiment(symptom_text)
    drug_scores = {}
    for r in cond_reviews:
        drug = r["drug"]
        if drug not in drug_scores:
            drug_scores[drug] = {"ratings": [], "sentiments": []}
        drug_scores[drug]["ratings"].append(r["rating"])
        drug_scores[drug]["sentiments"].append(analyze_sentiment(r["review"])["label"])

    results = []
    for drug, data in drug_scores.items():
        avg = sum(data["ratings"]) / len(data["ratings"])
        pos_ratio = data["sentiments"].count("Positive") / len(data["sentiments"])
        match_score = avg * 0.6 + pos_ratio * 4
        if sym_sentiment["label"] == "Negative":
            match_score *= 1.1  # boost drugs with strong positive reviews for bad symptoms
        results.append({
            "drug":        drug,
            "score":       round(match_score, 2),
            "avg_rating":  round(avg, 1),
            "match_pct":   round(pos_ratio * 100),
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:5]


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    conditions = sorted(set(r["condition"] for r in REVIEWS))
    return render_template("index.html", conditions=conditions)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/api/sentiment", methods=["POST"])
def api_sentiment():
    data = request.get_json()
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"error": "No text provided"}), 400
    return jsonify(analyze_sentiment(text))


@app.route("/api/condition_stats", methods=["POST"])
def api_condition_stats():
    data = request.get_json()
    condition = data.get("condition", "")
    stats = get_condition_stats(condition)
    if not stats:
        return jsonify({"error": "Condition not found"}), 404
    return jsonify(stats)


@app.route("/api/recommend", methods=["POST"])
def api_recommend():
    data = request.get_json()
    condition = data.get("condition", "")
    symptoms  = data.get("symptoms", "")
    recs = get_recommendations(condition, symptoms)
    return jsonify({"recommendations": recs})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
