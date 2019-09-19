import requests
from bs4 import BeautifulSoup
import func
def get_html():
    url='https://www.wunderground.com/weather/ru/moscow/55.76,37.62'
    r=requests.get(url)
    r=r.text
    return r
    
def get_temp():
    html=get_html()
    soup=BeautifulSoup(html,'lxml')
    temp=soup.select('div.current-temp')
    txt=temp[0].get_text()
    txt=func.chif(txt)
    return txt
#print(get_temp())