import requests
from bs4 import BeautifulSoup

keyword="로또당첨번호"
url="https://search.daum.net/nate?nil_suggest=btn&w=tot&DA=SBC&q="+keyword
data=requests.get(url)

if data.status_code != requests.codes.ok:
    print("접속실패")
    exit()

html=BeautifulSoup(data.text,"html.parser")
lottos_containter=html.select(".lottonum > span")

for lottos in lottos_containter:
    print(lottos.text)