import os
import requests
from bs4 import BeautifulSoup

# URL of the 2008 speech archive
base_url = "https://www.federalreserve.gov"
speech_index_url = f"{base_url}/newsevents/speech/2008speech.htm"

# Folder to save the speeches
os.makedirs("data/pulled", exist_ok=True)

# Get the index page
response = requests.get(speech_index_url)
soup = BeautifulSoup(response.content, "html.parser")

# Filter all <a> tags that look like speech links
speech_links = []
for a in soup.find_all("a", href=True):
    href = a["href"]
    if (
        href.startswith("/newsevents/speech/") and
        href.endswith(".htm") and
        "video" not in href and
        "press" not in href and
        "testimony" not in href and
        "transcript" not in href and
        "pdf" not in href
    ):
        full_url = base_url + href
        speech_links.append(full_url)

# Remove duplicates just in case
speech_links = list(set(speech_links))
print(f"✅ Found {len(speech_links)} valid 2008 speech links.")

# Download and save speech texts
for i, url in enumerate(speech_links, 1):
    speech_response = requests.get(url)
    speech_soup = BeautifulSoup(speech_response.content, "html.parser")
    
    # Extract title for filename (fallback to index)
    title_tag = speech_soup.find("h3")
    title = title_tag.text.strip() if title_tag else f"speech_{i}"
    filename = f"{title.lower().replace(' ', '_')[:50]}.txt"
    filepath = os.path.join("data/pulled", filename)

    # Extract main content of the speech
    paragraphs = speech_soup.find_all("p")
    speech_text = "\n".join(p.get_text(strip=True) for p in paragraphs)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(speech_text)

print("✅ All speeches downloaded and saved in 'data/pulled/'.")