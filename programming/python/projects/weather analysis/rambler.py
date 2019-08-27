import requests
from bs4 import BeautifulSoup

def get_html(url):
    r=requests.get(url)
    return r.text
def get_temp(html):
    soup=BeautifulSoup(html,'lxml')
    temp=soup.select('div._1HBR')
    txt=temp[0].get_text()
    return '+'+txt[0]+txt[1]
def main():
    url='https://weather.rambler.ru/v-moskve/now/'
    html=get_html(url)
    return get_temp(html)