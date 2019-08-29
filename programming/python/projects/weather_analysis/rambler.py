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
    html=get_html()
    soup=BeautifulSoup(html,'lxml')

    #Температура
    temp=soup.select('div._1HBR')
    txt1=temp[0].get_text()
    txt1='+'+txt1[0]+txt1[1]

    #Давление
    bar=soup.select('span._1DZh')
    txt2=bar[1].get_text()
    txt2=txt2[9]+txt2[10]+txt2[11]

    #Ветер
    wind=soup.select('span._1DZh')
    txt3=wind[0].get_text()
    txt3=txt3[6]

    #Записываем все в массим для удобства
    itog=[txt1,' ',txt2,' ',txt3]
    
    return(itog)