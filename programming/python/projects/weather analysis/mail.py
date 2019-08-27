import requests
from bs4 import BeautifulSoup

def get_html(url):
    r=requests.get(url)
    return r.text
def get_temp(html):
    soup=BeautifulSoup(html,'lxml')
    temp=soup.select('div.day__temperature')
    txt=temp[2].get_text()
    return txt[0]+txt[1]+txt[2]
def main():
    url='https://pogoda.mail.ru/prognoz/moskva/27-august/#2019'
    html=get_html(url)
    return get_temp(html)
