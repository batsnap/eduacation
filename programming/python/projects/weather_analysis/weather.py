import requests
from bs4 import BeautifulSoup
def get_html():
    url='https://weather.com/ru-RU/weather/today/l/55.75,37.58'
    r=requests.get(url)
    r=r.text
    return r
def get_temp():
    html=get_html()
    soup=BeautifulSoup(html,'lxml')
    temp=soup.select('div.today_nowcard-temp')
    txt=temp[0].get_text()
    #print(txt[0]+txt[1])
    return txt[0]+txt[1]
