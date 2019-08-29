import requests
from bs4 import BeautifulSoup

#Вытаскиваем html
def get_html():
    url='https://pogoda.mail.ru/prognoz/moskva/'
    r=requests.get(url)
    r=r.text
    return r

#Берём данные температуры, влажности и давление и ложим в массив.
def get_temp():
    html=get_html()
    soup=BeautifulSoup(html,'lxml')

    #Температура
    temp=soup.select('div.information__content__temperature')
    txt1=temp[0].get_text()
    txt1=txt1[1]+txt1[2]+txt1[3]

    #Влажность
    wet=soup.select('div.information__content__additional__item')
    txt2=wet[3].get_text()
    txt2=txt2[2]+txt2[3]

    #Давление
    bar=soup.select('div.information__content__additional__item')
    txt3=bar[2].get_text()
    txt3=txt3[2]+txt3[3]+txt3[4]

    #Ветер
    wind=soup.select('div.information__content__additional__item')
    txt4=wind[4].get_text()
    txt4=txt4[2]

    #Записываем все в массим для удобства
    itog=[txt1,' ',txt3,' ',txt4,' ',txt2]
    
    return(itog)