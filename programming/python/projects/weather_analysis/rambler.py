import requests
from bs4 import BeautifulSoup
import func
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
    txt1=func.chif(txt1)

    #Давление
    bar=soup.select('span._1DZh')
    txt2=bar[1].get_text()
    txt2=func.chif(txt2)

    #Ветер
    wind=soup.select('span._1DZh')
    txt3=wind[0].get_text()
    txt3=func.chif(txt3)

    #Записываем все в массим для удобства
    itog=[txt1,' ',txt2,' ',txt3]
    
    return(itog)
#print(get_temp())