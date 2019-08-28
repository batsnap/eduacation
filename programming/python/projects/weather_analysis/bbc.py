import requests
from bs4 import BeautifulSoup

def get_html():
    url='https://www.bbc.com/weather/524901'
    r=requests.get(url)
    r=r.text
    return r
def get_temp():
    html=get_html()
    soup=BeautifulSoup(html,'lxml')
    temp=soup.select('span.wr-value--temperature--c')
    txt=temp[0].get_text()
    return txt[0]
#get_temp()
