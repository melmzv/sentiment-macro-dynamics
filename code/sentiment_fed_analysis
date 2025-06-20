from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict
import statistics

# === Setup ===
analyzer = SentimentIntensityAnalyzer()
speech_scores = {}
speech_dates = {}

# === Helper Functions ===
def extract_date_from_text(text):
    for line in text.splitlines():
        try:
            return datetime.strptime(line.strip(), "%B %d, %Y")
        except ValueError:
            continue
    return None

def clean_speech_text(text):
    stop_phrases = ["References", "Footnotes", "Appendix", "Disclaimer"]
    lines = text.splitlines()
    start_index = next((i for i, line in enumerate(lines) if extract_date_from_text(line)), 0)
    lines = lines[start_index:]
    cleaned = []
    for line in lines:
        if any(phrase.lower() in line.lower() for phrase in stop_phrases):
            break
        cleaned.append(line.strip())
    return " ".join(cleaned)

# === Read and Process Files ===
input_dir = "data/pulled"
for filename in os.listdir(input_dir):
    if filename.endswith(".txt"):
        with open(os.path.join(input_dir, filename), "r", encoding="utf-8") as f:
            text = f.read()
            date = extract_date_from_text(text)
            if date:
                speech_dates[filename] = date
                cleaned_text = clean_speech_text(text)
                score = analyzer.polarity_scores(cleaned_text)
                speech_scores[filename] = score["compound"]

# === Display Sentiment Scores in Terminal ===
print("=== Sentiment Scores for Fed Speeches in 2008 ===")
for filename, date in sorted(speech_dates.items(), key=lambda x: x[1]):
    score = speech_scores[filename]
    print(f"{date.strftime('%Y-%m-%d')}: {filename} → Sentiment: {score:.3f}")
print("=================================================")

# === Prepare Output Directory ===
os.makedirs("data/generated", exist_ok=True)

# === Figure 1: Sentiment Over Time (Individual Speeches) ===
sorted_items = sorted(speech_scores.items(), key=lambda x: speech_dates[x[0]])
dates_sorted = [speech_dates[k].strftime("%b %d") for k, _ in sorted_items]
scores_sorted = [v for _, v in sorted_items]

plt.figure(figsize=(12, 5))
plt.plot(dates_sorted, scores_sorted, marker='o')
plt.title("Sentiment of Individual Fed Speeches in 2008", fontsize=14)
plt.xlabel("Speech Date", fontsize=12)
plt.ylabel("Compound Sentiment Score (VADER)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("data/generated/figure_individual_speeches.png")
plt.close()

# === Figure 2: Quarterly Mean and Median Sentiment ===
quarterly_scores = defaultdict(list)
for filename, date in speech_dates.items():
    quarter = f"Q{((date.month - 1) // 3) + 1}"
    quarterly_scores[quarter].append(speech_scores[filename])

quarters = sorted(quarterly_scores.keys())
mean_scores = [sum(quarterly_scores[q]) / len(quarterly_scores[q]) for q in quarters]
median_scores = [statistics.median(quarterly_scores[q]) for q in quarters]

x = range(len(quarters))
width = 0.35

plt.figure(figsize=(10, 6))
plt.bar([i - width/2 for i in x], mean_scores, width=width, label="Mean", color="skyblue")
plt.bar([i + width/2 for i in x], median_scores, width=width, label="Median", color="lightcoral")

plt.title("Quarterly Fed Speech Sentiment: Mean vs. Median (2008)", fontsize=14)
plt.xlabel("Quarter", fontsize=12)
plt.ylabel("Sentiment Score (VADER)", fontsize=12)
plt.xticks(x, quarters)
plt.grid(axis='y')
plt.legend()
plt.tight_layout()
plt.savefig("data/generated/figure_quarterly_mean_median.png")
plt.close()