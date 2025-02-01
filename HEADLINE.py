import requests
from bs4 import BeautifulSoup

# 네이버 뉴스 URL
url = 'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm'

# 네이버 뉴스 페이지를 요청
response = requests.get(url)
response.raise_for_status()  # 오류 발생 시 알림

# 페이지의 HTML을 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 헤드라인 뉴스 추출
headlines = soup.find_all('a', class_='news_title')

# 추출된 헤드라인 뉴스 출력
for headline in headlines:
    print(headline.text.strip())
