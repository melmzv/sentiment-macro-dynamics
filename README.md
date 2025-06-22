# The Signaling Channel of QE during the Global Financial Crisis: Evidence from Fed Communication Tone

This repository is part of the seminar **“New Regimes of Monetary Policy”** at **DIW Berlin (German Institute for Economic Research)**. It accompanies the theoretical and analytical study of the **2008 Global Financial Crisis**, with a particular focus on **Quantitative Easing (QE)** and the **signaling channel** of central bank communication.

The project investigates the **evolution of tone in Federal Reserve speeches during 2008**, using natural language processing (NLP) tools. It aims to detect whether shifts in sentiment reflect monetary policy stances and crisis severity during the early stages of QE.

This analytical prototype is not only relevant for speech analysis of the Fed but can be extended to:

- Other Fed communication channels (e.g., testimonies, FOMC press conferences),
- International central banks (e.g., **European Central Bank**),
- Broader macro-financial event detection pipelines.


## 🧠 What Does This Repo Do?

- Scrapes all 2008 Fed speeches from the [official website](https://www.federalreserve.gov/newsevents/speech/2008speech.htm)
- Applies sentiment analysis using the **VADER** lexicon ([GitHub Repo](https://github.com/cjhutto/vaderSentiment))
- Aggregates and visualizes tone dynamics across **time**, **individual policymakers**, and **quarters**
- Supports interpretation of **communication shifts** during key policy moments, e.g., Lehman Brothers collapse or first QE programs

The approach uses **NLP** methods to quantify tone and leverages Python for reproducibility and extension.



## 📈 Results

This section presents the three key visualizations generated from the tone analysis of 2008 Fed speeches. The sentiment scores were computed using **VADER**, an NLP tool designed for capturing tone in social and economic contexts.


<p align="center">
  <img src="data/generated/Figure_tone_over_time.png" alt="Tone Over Time" width="800"/>
  <br><em><strong>Figure 1:</strong> Daily average sentiment scores (compound polarity) for all Fed speeches in 2008. Notable drops in tone can be observed around key crisis dates, such as the Bear Stearns bailout in March and the Lehman collapse in September. The gradual recovery of tone toward December coincides with stronger forward guidance and unconventional easing communication. This graph reflects the Fed’s tone trajectory under rising financial stress.</em>
</p>


<p align="center">
  <img src="data/generated/Figure_tone_by_speaker.png" alt="Tone by Speaker" width="850"/>
  <br><em><strong>Figure 2:</strong> Average sentiment score by Fed speaker in 2008. Chairman Ben Bernanke shows a consistently more negative tone than other governors, likely reflecting his role during high-stakes interventions. Other members such as Kohn and Yellen maintain relatively neutral language. These differences hint at individual communication styles and leadership roles during crisis response.</em>
</p>


<p align="center">
  <img src="data/generated/Figure_quarterly_tone.png" alt="Quarterly Tone Shift" width="700"/>
  <br><em><strong>Figure 3:</strong> Quarterly average tone of Fed speeches in 2008. The steep decline from Q1 to Q3 underscores the worsening financial outlook, culminating in QE announcements. The partial rebound in Q4 suggests a communication shift toward reassurance and signaling of long-term policy commitment. This chart supports the hypothesis that tone evolves with both market conditions and policy signaling goals.</em>
</p>


## 💡 Summary

This prototype provides empirical evidence on how **central bank tone** evolved during the pivotal year of 2008. It uses a **transparent NLP pipeline** to trace tone dynamics at high resolution – by day, by speaker, and by quarter.

Its modular structure allows for future extensions:
- Comparing **Fed speeches vs. testimonies**
- Cross-institutional tone studies (e.g., ECB, BoE)
- Enhancing with **topic modeling** or **machine learning classifiers** beyond lexicon methods

The work contributes to ongoing research on central bank transparency, credibility, and the signaling power of monetary policy communication.


## 🔁 Reproducibility

To run the full pipeline and regenerate plots:

1. Clone the repository  
2. Create a virtual environment:  
   ```bash
   python3 -m venv venv && source venv/bin/activate
3. Install dependencies by running `pip install -r requirements.txt` in the terminal
4. Run `make all` in the terminal


# 📚 Suggested Readings & References
- VADER Sentiment Analysis Repo: https://github.com/cjhutto/vaderSentiment
- Federal Reserve 2008 Speeches: https://www.federalreserve.gov/newsevents/speech/2008speech.htm
- Fratzscher, M., & Rieth, M. (2019). Monetary Policy, Innovation and Productivity: Evidence from the Euro Area. DIW Discussion Paper.
- Hansen, S., McMahon, M., & Prat, A. (2018). Transparency and Deliberation within the FOMC: A Computational Linguistics Approach. Quarterly Journal of Economics.
- Schmeling, M., & Wagner, C. (2019). Does Central Bank Tone Move Asset Prices? International Journal of Central Banking.

# Licensing
The repository is licensed under the MIT license.
Contributions and extensions are welcome — especially from researchers at DIW Berlin, ECB, or other macro-finance research communities. :raised_hands: