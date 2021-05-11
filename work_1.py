# 네이버 TV 인기영상 1 ~ 100위 정보 수집하기
import requests
from bs4 import BeautifulSoup


raw = requests.get("https://tv.naver.com/r")
html = BeautifulSoup(raw.text, "html.parser")

# div.inner: 네이버 TV 1~3위 영상을 가리키는 선택자
clips = html.select("dl.cds_info")

for clip in clips:
    # 데이터 수집부분
    title = clip.select_one("dt.title")
    chn = clip.select_one("dd.chn")
    hit = clip.select_one("span.hit")
    like = clip.select_one("span.like")

    # 수집 결과 출력부분
    print(f'제목: {title.text.strip()}')
    print(f'채널명: {chn.text.strip()}')
    print(hit.text.strip())
    print(like.text.strip())

    print('-' * 50)
