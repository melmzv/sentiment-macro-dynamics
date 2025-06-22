from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
import matplotlib.pyplot as plt

# Initialize
analyzer = SentimentIntensityAnalyzer()
results = {}

# Loop through all files
for filename in os.listdir("data/external"):
    if filename.endswith(".txt"):
        with open(f"data/external/{filename}", "r", encoding="utf-8") as f:
            text = f.read()
            score = analyzer.polarity_scores(text)
            results[filename] = score["compound"]

# Define the desired chronological order and axis labels
desired_order = ["jan_10_2008.txt", "mar_14_2008.txt", "sep_23_2008.txt", "dec_01_2008.txt"]
labels = [
    "Jan 10 2008 – Economic Outlook",
    "Mar 14 2008 – Mortgage Crisis Response",
    "Sep 23 2008 – Market Panic",
    "Dec 01 2008 – QE1 Announcement"
]

# Filter and reorder results based on desired order
ordered_scores = [results[fn] for fn in desired_order if fn in results]
ordered_labels = [labels[i] for i, fn in enumerate(desired_order) if fn in results]

# Print sentiment scores to terminal
print("=== Sentiment Scores for Selected Fed Speeches ===")
for i, fn in enumerate(desired_order):
    if fn in results:
        print(f"{labels[i]}: {results[fn]:.3f}")
print("===================================================")

# Create output folder if it doesn't exist
os.makedirs("data/generated", exist_ok=True)

# Plot and save
plt.figure(figsize=(10, 5))
plt.plot(ordered_labels, ordered_scores, marker='o')
plt.title("Evolution of Federal Reserve Communication Tone During the 2008 Crisis", fontsize=14)
plt.xlabel("Speech Date and Thematic Focus", fontsize=12)
plt.ylabel("Compound Sentiment Score (VADER)", fontsize=12)
plt.grid(True)
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("data/generated/tone_plot.png")
plt.show()