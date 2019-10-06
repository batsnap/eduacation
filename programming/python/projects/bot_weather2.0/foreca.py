import requests
from bs4 import BeautifulSoup

#Прием странницы
def get_html():
    url='https://www.foreca.ru/Russia/Moskva?obshist'
    r=requests.get(url)
    r=r.text
    return r

def get_danie():
    f=open('test.txt','w')
    html=get_html()
    soup=BeautifulSoup(html,'lxml')
    temp=soup.find_all('strong')
    print(temp)
    for i in range(len(temp)):
        test=temp[i].get_text()
        f.write(test+'\n')
get_danie()