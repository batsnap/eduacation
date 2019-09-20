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
    html=get_html()
    soup=BeautifulSoup(html,'lxml')
    table=soup.find('table',id='theProxyList')
    proxy=table.find_all('td')
    for i in range(len(proxy)):
        text=proxy[i].get_text()
        if len(text)>11 and len(text)<16 and check(text):
            text2=proxy[i+1].get_text()
            f.write(text+':'+text2+'\n')
        
get_proxy()