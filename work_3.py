import requests
from bs4 import BeautifulSoup


for p in range(1, 4):
    raw = requests.get(f"https://news.ycombinator.com/news?p={p}",
                       headers={"User-Agent": "Mozilla/5.0"})
    html = BeautifulSoup(raw.text, "html.parser")
    articles = html.select("tr.athing")

    for article in articles:
        rank = article.select_one("span.rank").text
        title = article.select_one("a.storylink").text

        print(rank, title)
