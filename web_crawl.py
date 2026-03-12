import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

start_url = "https://ismailyusufcollege.ac.in/"

visited = set()
index = {}

response = requests.get(start_url)
soup = BeautifulSoup(response.text, "html.parser")

links = []

# collect first few links
for a in soup.find_all("a", href=True):
    link = urljoin(start_url, a['href'])
    if link not in links:
        links.append(link)

# crawl first 3 pages
for url in links[:10]:
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        words = soup.get_text().lower().split()

        for w in words:
            if w not in index:
                index[w] = []
            if url not in index[w]:
                index[w].append(url)

    except:
        pass

print("\nSample Inverted Index:\n")

for word, pages in list(index.items())[:10]:
    print(f"{word:<15} ->")
    for p in pages:
        print("   ", p)
    print()