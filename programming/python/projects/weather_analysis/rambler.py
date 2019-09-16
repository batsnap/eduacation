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
    chisla='01234567890'
    html=get_html()
    soup=BeautifulSoup(html,'lxml')

    #Температура
    temp=soup.select('div._1HBR')
    txt1=temp[0].get_text()
    txt1='+'+txt1[0]+txt1[1]

    #Давление
    bar=soup.select('span._1DZh')
    txt2=bar[1].get_text()
    print(txt2)
    txt22=''
    for i in range(len(txt2)):
        if txt2[i] in chisla:
            txt22+=txt2[i]
    txt2=txt22

    #Ветер
    wind=soup.select('span._1DZh')
    txt3=wind[0].get_text()
    txt3=txt3[6]

    #Записываем все в массим для удобства
    itog=[txt1,' ',txt2,' ',txt3]
    
    return(itog)
print(get_temp())