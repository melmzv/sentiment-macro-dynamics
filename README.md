# The Signaling Channel of QE during the Global Financial Crisis: Evidence from Fed Communication Tone

This repository forms part of the graduate seminar **“New Regimes of Monetary Policy”** at **DIW Berlin (German Institute for Economic Research)**, held under the supervision of Prof. Marcel Fratzscher, Ph.D. It accompanies the theoretical and analytical study of the **2008 Global Financial Crisis**, with a particular focus on **Quantitative Easing (QE)** and the **signaling channel** of central bank communication.

The project investigates the **evolution of tone in Federal Reserve speeches during 2008**, using natural language processing (NLP) tools. It aims to detect whether shifts in sentiment reflect monetary policy stances and crisis severity during the early stages of QE. This repo is designed for researchers, students, and policymakers interested in the intersection of monetary policy, NLP, and financial crises.

This analytical framework contributes to the growing literature on central bank communication as a policy instrument, demonstrating how sentiment analysis can uncover latent signals in qualitative data. While the current implementation focuses on the Federal Reserve in 2008, the methodology is generalizable and may be extended to:

- Other Fed communication channels (e.g., testimonies, FOMC press conferences),
- International central banks (e.g., **European Central Bank**),
- Broader macro-financial event detection pipelines.


## 🧠 What Does This Repo Do?

- Scrapes all 2008 Fed speeches from the [official website](https://www.federalreserve.gov/newsevents/speech/2008speech.htm)
- Applies sentiment analysis using the **VADER** lexicon - [GitHub Repo](https://github.com/cjhutto/vaderSentiment)
- Aggregates and visualizes tone dynamics across **time**, **individual policymakers**, and **quarters**
- Supports interpretation of **communication shifts** during key policy moments, e.g., Lehman Brothers collapse or first QE programs

The approach uses **NLP** methods to quantify tone and leverages Python for reproducibility and extension.



## 📈 Results

This section presents the three key visualizations generated from the tone analysis of 2008 Fed speeches. The sentiment scores were computed using **VADER**, an NLP tool designed for capturing tone in social and economic contexts.


<p align="center">
  <img src="data/generated/figure_individual_speeches.png" alt="Sentiment of Individual Fed Speeches in 2008" width="850"/>
  <br><em><strong>Figure 1:</strong> Sentiment scores (compound VADER polarity) of individual Federal Reserve speeches in 2008. While the majority of speeches express highly positive tone (close to +1), several speeches around key market panic episodes - especially in March, June, and September - exhibit sharp drops to neutral or negative territory. This graph captures the volatility and urgency in tone during the most critical phases of the financial crisis.</em>
</p>


<p align="center">
  <img src="data/generated/figure_quarterly_mean_median.png" alt="Quarterly Sentiment of Fed Speeches" width="800"/>
  <br><em><strong>Figure 2:</strong> Quarterly average (blue) and median (red) sentiment scores of all Fed speeches in 2008. The data show a notable decline in average tone from Q1 to Q3, with a recovery in Q4, aligning with the timeline of quantitative easing (QE1) announcements. Interestingly, the median sentiment remains consistently high across all quarters, indicating that only a subset of speeches drove the average sentiment drop - likely those given by central figures at pivotal crisis moments.</em>
</p>


<p align="center">
  <img src="data/generated/tone_plot.png" alt="Tone Evolution for Key Speeches" width="800"/>
  <br><em><strong>Figure 3:</strong> Evolution of tone for four landmark Fed speeches in 2008, each tied to a distinct policy or market event. Tone drops significantly between January and September, reflecting worsening market conditions and escalating interventions. The final speech (QE1 announcement in December) marks a sharp rebound in sentiment score, suggesting deliberate use of tone to support credibility and calm markets during extraordinary easing.</em>
</p>


## 💡 Discussion

This prototype provides empirical evidence on how **Federal Reserve tone** evolved during the pivotal year of 2008. It uses a **transparent NLP pipeline** to trace tone dynamics at high resolution – by pivotal event, by individual speech, and by quarter.

Its modular structure allows for future extensions:
- Comparing **Fed speeches vs. testimonies**
- Cross-institutional tone studies (e.g., ECB, BoE)
- Enhancing with **topic modeling** or **machine learning classifiers** beyond lexicon methods

The work contributes to ongoing research on central bank transparency, credibility, and the signaling power of monetary policy communication.


# 🔁 Reproducibility

To run the full pipeline and regenerate plots:

1. Clone the repository  
2. Create a virtual environment:  
   ```bash
   python3 -m venv venv && source venv/bin/activate
3. To run the complete workflow in one click: 
   ```bash
   pip install -r requirements.txt
   make all
   ```


# 📚 Suggested Readings & References
- VADER Sentiment Analysis Repo: https://github.com/cjhutto/vaderSentiment
- Federal Reserve 2008 Speeches: https://www.federalreserve.gov/newsevents/speech/2008speech.htm
- Ehrmann, M., & Fratzscher, M. (2007). Communication by central bank committee members: different strategies, same effectiveness? Journal of Money, Credit and Banking, 39(2‐3), 509–541.
- Hansen, S., McMahon, M., & Prat, A. (2018). Transparency and Deliberation within the FOMC: A Computational Linguistics Approach. Quarterly Journal of Economics.
- Schmeling, M., & Wagner, C. (2025). Does Central Bank Tone Move Asset Prices? Journal of Financial and Quantitative Analysis.

# Licensing
The repository is licensed under the MIT license.

Contributions and extensions are welcome - especially from researchers at DIW Berlin, ECB, or other macro-finance research communities. :raised_hands: