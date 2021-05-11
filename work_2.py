import requests
from bs4 import BeautifulSoup


keyword = input("키워드 입력: ")

for n in range(1, 100, 10):
    raw = requests.get(f"https://search.naver.com/search.naver?where=news&query={keyword}&start={str(n)}",
                       headers={'User-Agent': 'Mozilla/5.0'})
    html = BeautifulSoup(raw.text, "html.parser")
    articles = html.select("ul.list_news > li")

    # 기사에 대한 제목/언론사를 수집
    for article in articles:
        title = article.select_one("a.news_tit").text
        source = article.select_one("a.info.press").text
        print(title, source)
