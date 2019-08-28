import requests
from bs4 import BeautifulSoup
def get_html():
    url='https://yandex.ru/pogoda/moscow'
    r=requests.get(url)
    r=r.text
    return r
def get_temp():
    html=get_html()
    soup=BeautifulSoup(html,'lxml')
    temp=soup.select('span.temp__value')
    txt=temp[0].get_text()
    return txt
