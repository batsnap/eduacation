import requests
from bs4 import BeautifulSoup
import func

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
    txt1=temp[29].get_text()
    txt1=func.chif(txt1)

    #Давление
    bar_wet=soup.select('dd.wr-time-slot-secondary__value.gel-long-primer-bold')
    txt2=bar_wet[1].get_text()
    txt2=func.chif(txt2)
    txt2=str((float(txt2[0]+txt2[1]+txt2[2]+txt2[3]))*0.750062)
    
    #Ветер
    wind=soup.select('span.wr-value--windspeed.wr-value--windspeed--mph')
    txt3=wind[29].get_text()
    txt3=func.chif(txt3)

    #Влажность
    txt4=bar_wet[0].get_text()
    txt4=func.chif(txt4)
    
    #Итог
    itog=[txt1,' ',txt2,' ',txt3,' ',txt4]
    
    return itog
#print(get_temp())