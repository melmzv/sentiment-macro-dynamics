# --- Header -------------------------------------------------------------------
# Automates scraping, sentiment analysis, and figure generation
# If you are new to Makefiles: https://makefiletutorial.com
# (C) Mel Mzv - See LICENSE file for details
# ------------------------------------------------------------------------------
.PHONY: all clean very-clean

# --- Output targets ---
TONE_PLOT := data/generated/tone_plot.png
INDIVIDUAL_PLOT := data/generated/figure_individual_speeches.png
QUARTERLY_PLOT := data/generated/figure_quarterly_mean_median.png

all: $(TONE_PLOT) $(INDIVIDUAL_PLOT) $(QUARTERLY_PLOT)

# --- Step 1: Scrape Fed Speeches ---
data/pulled:
	python code/scrape_fed_speeches.py

# --- Step 2: Tone Evolution from External Files ---
$(TONE_PLOT): code/sentiment_tone_evolution.py
	python $<

# --- Step 3: Analyze Speech Sentiment by Date and Quarter ---
$(INDIVIDUAL_PLOT) $(QUARTERLY_PLOT): code/sentiment_individual_quarterly_2008.py data/pulled
	python $<

# --- Clean generated figures only ---
clean:
	rm -f $(TONE_PLOT) $(INDIVIDUAL_PLOT) $(QUARTERLY_PLOT)

# --- Remove everything including scraped speech files ---
very-clean: clean
	rm -rf data/pulled