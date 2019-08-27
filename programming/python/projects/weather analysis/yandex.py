import requests
from bs4 import BeautifulSoup
def get_html(url):
    r=requests.get(url)
    return r.text
def get_temp(html):
    soup=BeautifulSoup(html,'lxml')
    temp=soup.select('span.temp__value')
    txt=temp[3].get_text()
    return txt
def main():
    url='https://yandex.ru/pogoda/moscow/details?via=ms#27'
    html=get_html(url)
    return get_temp(html)

