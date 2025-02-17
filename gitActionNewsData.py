import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd
import ssl
import urllib3


ssl._create_default_https_context = ssl._create_unverified_context
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
titleList = []

for j in range(1, 11, 1):
    res = req.get("https://search.daum.net/search?w=news&nil_search=btn&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=%EC%86%8D%EB%B3%B4&p=" + str(j), verify=False)
    soup = bs(res.text, "lxml")
    title = soup.select("div.item-title > strong > a ")

    for i in title :
        titleList.append(i.text)

dic = {"newsTitle" : titleList}
df = pd.DataFrame(dic)
df.to_csv("newsTitle.csv", encoding="utf-8-sig", index=False)
