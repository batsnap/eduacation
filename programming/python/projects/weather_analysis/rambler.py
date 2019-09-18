import requests
from bs4 import BeautifulSoup

#вытаскиваем html
def get_html():
    url='https://weather.rambler.ru/v-moskve/now/'
    r=requests.get(url)
    r=r.text
    return r

#Берём данные температуры, влажности и давление и ложим в массив.
def get_temp():
    chisla='0123456789'
    html=get_html()
    soup=BeautifulSoup(html,'lxml')

    #Температура
    temp=soup.select('div._1HBR')
    txt1=temp[0].get_text()
    txt11=''
    for i in range(len(txt1)):
        if txt1[i] in chisla:
            txt11+=txt1[i]
    txt1=txt11

    #Давление
    bar=soup.select('span._1DZh')
    txt2=bar[1].get_text()
    txt22=''
    for i in range(len(txt2)):
        if txt2[i] in chisla:
            txt22+=txt2[i]
    txt2=txt22

    #Ветер
    wind=soup.select('span._1DZh')
    txt3=wind[0].get_text()
    txt33=''
    for i in range(len(txt3)):
        if txt3[i] in chisla:
            txt33+=txt3[i]
    txt3=txt33

    #Записываем все в массим для удобства
    itog=[txt1,' ',txt2,' ',txt3]
    
    return(itog)
#print(get_temp())