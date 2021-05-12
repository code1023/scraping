# 네이버 e북 인기 TOP100 데이터 수집
import requests
from bs4 import BeautifulSoup


for n in range(1, 6):
    raw = requests.get(f"https://series.naver.com/ebook/top100List.nhn?page={n}",
                       headers={"User-Agent": "Mozilla/5.0"})
    html = BeautifulSoup(raw.text, "html.parser")

    books = html.select("div.lst_thum_wrap li")

    for book in books:
        rank = book.select_one("span.num").text
        title = book.select_one("a strong").text
        author = book.select_one("span.writer").text

        print(f"{rank}. {title} - {author}")
