import requests
from bs4 import BeautifulSoup

lotto_url = 'https://dhlottery.co.kr/common.do?method=main'

res = requests.get(lotto_url)

soup = BeautifulSoup(res.text, 'html.parser')

balls = soup.select('span.ball_645')
for ball in balls:
    print(ball.text)