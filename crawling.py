from bs4 import BeautifulSoup
from pymongo import MongoClient
import requests
import time
import html5lib
mongo = MongoClient("localhost",20000)

def mongo_save(mongo, datas, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_many(datas).inserted_ids
    return result

navers=[]
aid=1

IsNotEnd=True
faultcount=0

# header안붙이고 쓰다가 봇으로 인식당할 가능성이 있음
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

while(IsNotEnd):
    conversion_aid = '{0:010d}'.format(aid)
    try:
        html = requests.get(
            f"https://entertain.naver.com/read?oid=005&aid={conversion_aid}&sid=100",headers=headers)
        faultcount +=1
        
        
        
        if(html.status_code==200):
            
            soup= BeautifulSoup(html.text, 'html.parser')
            
            temp_title=soup.select("#content > div.end_ct > div > h2")[0]
            print(temp_title)
            title= temp_title.contents[0].strip()
            company = soup.select(".press_logo > img")[0]["alt"]
            
            aid+=1
            dict = {"title": title, "company": company}
            navers.append(dict)
            print(len(navers))
        if faultcount>20:
            IsNotEnd =False
        
    except Exception as e:
        print(e)
        pass
mongosave = mongo_save(mongo, navers, "greendb", "navers")
print (mongosave)
print("complete")
