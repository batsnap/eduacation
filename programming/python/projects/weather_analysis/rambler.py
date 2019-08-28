import requests
from bs4 import BeautifulSoup

def get_html():
    url='https://weather.rambler.ru/v-moskve/now/'
    r=requests.get(url)
    r=r.text
    return r
def get_temp():
    html=get_html()
    soup=BeautifulSoup(html,'lxml')
    temp=soup.select('div._1HBR')
    txt=temp[0].get_text()
    return '+'+txt[0]+txt[1]
