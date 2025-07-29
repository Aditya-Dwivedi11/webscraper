import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import argparse

def fetch_page(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
    except Exception as e:
        print(f"[ERROR] Failed to fetch {url}:\n{e}")
        return None

def extract_products(soup):
    data = []
    for item in soup.select('.thumbnail'):
        title = item.select_one('.title')
        price = item.select_one('.price')

        if title and price:
            data.append({
                'title': title.text.strip(),
                'price': price.text.strip()
            })
    return data

def save_to_csv(data, filename=None):
    if not data:
        print("[INFO] No data to save.")
        return
    if not filename:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"products_{timestamp}.csv"

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"[✓] {len(data)} products saved to '{filename}'")

def run_scraper(url):
    print(f"[INFO] Scraping: {url}")
    soup = fetch_page(url)
    if soup:
        data = extract_products(soup)
        save_to_csv(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Web scraper for product listings.")
    parser.add_argument('url', help='Target URL to scrape')
    args = parser.parse_args()

    run_scraper(args.url)
