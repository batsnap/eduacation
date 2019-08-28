import requests
from bs4 import BeautifulSoup

def get_html():
    url='https://pogoda.mail.ru/prognoz/moskva/'
    r=requests.get(url)
    r=r.text
    return r
def get_temp():
    html=get_html()
    soup=BeautifulSoup(html,'lxml')
    temp=soup.select('div.information__content__temperature')
    txt=temp[0].get_text()
    #print(txt[1]+txt[2]+txt[3])
    return txt[1]+txt[2]+txt[3]
#main()