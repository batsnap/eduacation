import requests
from bs4 import BeautifulSoup

#Прием странницы
def get_html():
    url='https://www.bbc.com/weather/524901'
    r=requests.get(url)
    r=r.text
    return r

#
def get_temp():
    html=get_html()
    soup=BeautifulSoup(html,'lxml')

    #Температура
    temp=soup.select('span.wr-value--temperature--c')
    txt1=temp[27].get_text()
    txt1=txt1[0]+txt1[1]

    #Давление
    bar_wet=soup.select('dd.wr-time-slot-secondary__value.gel-long-primer-bold')
    txt2=bar_wet[1].get_text()
    txt2=str((float(txt2[0]+txt2[1]+txt2[2]+txt2[3]))*0.750062)
    
    #Ветер
    wind=soup.select('span.wr-value--windspeed.wr-value--windspeed--mph')
    txt3=wind[29].get_text()
    txt3=txt3[0]

    #Влажность
    txt4=bar_wet[0].get_text()
    txt4=txt4[0]+txt4[1]
    
    #Итог
    itog=[txt1,' ',txt2,' ',txt3,' ',txt4]
    
    return itog
