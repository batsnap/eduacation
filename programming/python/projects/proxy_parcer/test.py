import requests
from bs4 import BeautifulSoup
def check(s):
    chif='01234567890.'
    i=0
    while i<len(s):
        if s[i] in chif:
            i+=1
        else:
            return False
    if i==len(s):
        return True


def get_html():
    url='http://foxtools.ru/Proxy'
    r=requests.get(url)
    r=r.text
    return r
def get_proxy():
    f = open('proxy_list.txt', 'w')
    html=open('test.html').read()
    soup=BeautifulSoup(html,'lxml')
    table=soup.find('table',class_='podbor')
    proxy=table.find_all('td')
    for i in range(6,len(proxy),5):
        text=proxy[i].get_text()
        f.write(text+'\n')
    f.close()
get_proxy()