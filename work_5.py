# 다음뉴스 기사 데이터 수집하기
import requests
from bs4 import BeautifulSoup


search = input("검색어 입력: ")
for n in range(1, 5):
    raw = requests.get(f"https://search.daum.net/search?w=news&q={search}&p={n}")
    html = BeautifulSoup(raw.text, "html.parser")
    articles = html.select("div.wrap_cont")

    for article in articles:
        title = article.select_one("a.f_link_b").text
        source = article.select_one("span.f_nb.date").text
        summary = article.select_one("p.f_eb.desc").text

        print(f"{title} | {source}")
        print(summary)

        print("="*50)
