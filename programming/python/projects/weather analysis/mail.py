import requests
from bs4 import BeautifulSoup

def get_html(url):
    r=requests.get(url)
    return r.text
def get_temp(html):
    soup=BeautifulSoup(html,'lxml')
    temp=soup.select('div.information__content__temperature')
    txt=temp[0].get_text()
    #print(txt[1]+txt[2]+txt[3])
    return txt[1]+txt[2]+txt[3]
def main():
    url='https://pogoda.mail.ru/prognoz/moskva/'
    html=get_html(url)
    return get_temp(html)
#main()