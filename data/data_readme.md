This `data_readme.md` documents the structure and purpose of the data used in the Fed Communication Sentiment Analysis project. This repository supports the reproducible analysis of Federal Reserve speeches during the 2008 financial crisis, focusing on sentiment trends and communication tone evolution.

The setup encourages a clean separation of code-generated data from externally sourced data. Only essential datasets that are not easily reproducible or are lightweight should be committed.

The directories are organized as follows:
- pulled: Contains raw speech text files scraped directly from the official [Federal Reserve website](https://www.federalreserve.gov/newsevents/speech/2008speech.htm). These speeches are from 2008 and saved as `.txt` files by running the scraping script.
Example contents:
- `assessing_the_potential_for_instability_in_financi.txt`
- `economic_outlook.txt`
> [!NOTE]
> This folder is populated automatically by running `python code/scrape_fed_speeches.py`

- external: Contains curated speech files manually selected for tone-tracking analysis. These are not generated programmatically and reflect key events in the crisis.
Example contents:
    - `jan_10_2008.txt` – Economic Outlook  
    - `mar_14_2008.txt` – Mortgage Crisis Response  
    - `sep_23_2008.txt` – Market Panic  
    - `dec_01_2008.txt` – QE1 Announcement

- generated: Contains all sentiment analysis results and visual outputs created by running the analysis scripts.
    Example outputs:
    - `figure_individual_speeches.png` – Sentiment over time (individual speeches)
    - `figure_quarterly_mean_median.png` – Average vs. median quarterly sentiment
    - `tone_plot.png` – Communication tone of key speeches during the crisis

> 🛠️ These are generated automatically by:
> - `code/sentiment_individual_quarterly_2008.py`
> - `code/sentiment_tone_evolution.py`

Note the following: :thinking:
- The `pulled/` and `generated/` folders are versioned intentionally to support transparency and reproducibility.
- The `.gitignore` rules in each subfolder were adapted to allow committed outputs (e.g., figures, key scraped content).

    