from pymongo import MongoClient
from pymongo.cursor import CursorType

import requests

from bs4 import BeautifulSoup

import datetime

# Mongo 연결
mongo = MongoClient("localhost", 20000)





navers = []
aid = 1  
result = 0


while True:

    aid_string = format(aid, '010')
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }
    # sid = 100 (정치) oid = 005 (국민일보)
    try:
        html = requests.get(
            f"https://entertain.naver.com/read?oid=005&aid={aid_string}&sid=100",headers=headers)

        if html.status_code == 200:

            soup = BeautifulSoup(html.text, 'html.parser')

            title = soup.select_one(".end_tit").text
            company = soup.select(".press_logo > img")[0]["alt"]
            createdAt = datetime.datetime.now()

            dict = {"title": title, "company": company, "createdAt": createdAt}
            navers.append(dict)
            print(len(navers))

            result += 1

        if result == 20:
            print("끝")
            break

        aid += 1

    except Exception as e:
        print("뭔가 잘못됨")
        pass

aaa = mongo_save(mongo, navers, "greendb", "navers")  # List안에 dict을 넣어야 함
print(aaa)