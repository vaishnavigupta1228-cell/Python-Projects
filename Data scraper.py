import requests
from bs4 import BeautifulSoup
import csv
import time

BASE_URL = "http://quotes.toscrape.com/page/{page}/"

def fetch_page(page):
    url = BASE_URL.format(page=page)
    headers = {"User-Agent": "Mozilla/5.0 (compatible; DataScraper/1.0)"}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        return r.text
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch {url}: {e}")
        return None

def parse_quotes(html):
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for quote_div in soup.select("div.quote"):
        text = quote_div.find("span", class_="text").get_text(strip=True)
        author = quote_div.find("small", class_="author").get_text(strip=True)
        tags = [t.get_text(strip=True) for t in quote_div.select("div.tags a.tag")]
        rows.append({"text": text, "author": author, "tags": ",".join(tags)})
    return rows

def save_to_csv(filename, rows):
    keys = ["text", "author", "tags"]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)

def main():
    all_rows = []
    # change range(1,4) to scrape more pages (be polite)
    for page in range(1, 4):
        print(f"Fetching page {page}...")
        html = fetch_page(page)
        if not html:
            print("Stopping due to fetch error.")
            break
        rows = parse_quotes(html)
        if not rows:
            print("No more quotes found; stopping.")
            break
        all_rows.extend(rows)
        time.sleep(1)  # polite delay between requests

    if all_rows:
        save_to_csv("quotes.csv", all_rows)
        print(f"Saved {len(all_rows)} rows to quotes.csv")
    else:
        print("No data scraped.")

if __name__ == "__main__":
    main()
