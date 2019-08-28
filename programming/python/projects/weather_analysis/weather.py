import requests
from bs4 import BeautifulSoup

def get_html(url):
    r=requests.get(url)
    return r.text
def get_temp(html):
    soup=BeautifulSoup(html,'lxml')
    temp=soup.select('div.today_nowcard-temp')
    txt=temp[0].get_text()
    #print(txt[0]+txt[1])
    return txt[0]+txt[1]
def main():
    url='https://weather.com/ru-RU/weather/today/l/55.75,37.58'
    html=get_html(url)
    return get_temp(html)
#main()