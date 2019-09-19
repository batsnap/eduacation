import requests
from bs4 import BeautifulSoup
import func
#вытаскиваем html
def get_html():
    url='https://weather.com/ru-RU/weather/today/l/55.75,37.58'
    r=requests.get(url)
    r=r.text
    return r

#Берём данные температуры, влажности и давление и ложим в массив.
def get_temp():
    html=get_html()
    soup=BeautifulSoup(html,'lxml')

    #Температура
    temp=soup.select('div.today_nowcard-temp')
    txt1=temp[0].get_text()
    txt1=func.chif(txt1)

    #Влажность
    all=soup.select('span')
    txt2=all[68].get_text()
    txt2=func.chif(txt2)

    #Давление
    txt3=all[72].get_text()
    txt3=func.chif(txt3)
    txt33=''
    for i in range(len(txt3)-1): 
        txt33+=txt3[i]
    txt3=txt33
    txt3=str(float(txt3)*0.750062)

    #Ветер
    txt4=all[67].get_text()
    if txt4=='Штиль':
        txt4='0'
    else:
        txt4=func.chif(txt4)
        txt4=str(float(txt4)/3.6)
    

    #Записываем все в массим для удобства
    itog=[txt1,' ',txt3,' ',txt4,' ',txt2]

    return(itog)
#print(get_temp())