import requests
from bs4 import BeautifulSoup

def get_html():
    url='http://free-proxy.cz/ru/proxylist/main/2'
    r=requests.get(url)
    r=r.text
    return r
def get_proxy():
    html=get_html()
    soup=BeautifulSoup(html,'lxml')
    proxy=soup.select('div.body_w')
    table=proxy[0].get_text()
    return table
print(get_proxy())