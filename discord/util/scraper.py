import requests
import re
from bs4 import BeautifulSoup

def getMatchesForToday():
    url = "https://www.flashscore.dk/tennis/"
    session = requests.Session()

    resp = session.get(url, timeout=30)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    spans = soup.select("span.next_round")
    text = "".join(s.get_text("", strip=True) for s in spans)
    x = re.split("^(\d{2}\.\d{2}\..*?)(?=\s\d{2}\.\d{2}\.|$)", text)
    clean_data = re.sub(r'^\d{2}\.\d{2}\.', '', x[1])
    matches_list = [match.strip() for match in clean_data.split(',') if match.strip()]
    return matches_list
