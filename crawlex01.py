import requests
from bs4 import BeautifulSoup

html = requests.get(
    "https://n.news.naver.com/mnews/article/005/0000000001?sid=100")

soup= BeautifulSoup(html.text, 'html.parser')

weather_el = soup.select_one("#ct > div.media_end_head.go_trans > div.media_end_head_title > h2")

print(weather_el.text)
