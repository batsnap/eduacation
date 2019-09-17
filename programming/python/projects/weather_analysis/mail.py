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
    chif='0123456789+-'
    temp=soup.select('div.information__content__temperature')
    txt1=temp[0].get_text()
    txt11=''
    for i in range(len(txt1)):
        if txt1[i] in chif:
            txt11+=txt1[i]
    txt1=txt11

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
#print(get_temp())