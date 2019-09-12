import requests
from bs4 import BeautifulSoup

def get_html():
    url='https://yandex.ru/pogoda/moscow'
    r=requests.get(url)
    r=r.text
    return r

#Берём данные температуры, влажности и давление и ложим в массив.
def get_temp():
    html=get_html()
    soup=BeautifulSoup(html,'lxml')

    #Температура
    temp=soup.select('span.temp__value')
    txt1=temp[0].get_text()

    #Ветер
    all=soup.select('dd.term__value')
    txt2=all[2].get_text()
    txt2=txt2[0]+'.'+txt2[2]
    if txt2=='Ш.и':
        txt2='0'
    else:
        txt2=txt2[0]+'.'+txt2[2]

    #Влажность
    txt3=all[3].get_text()
    txt3=txt3[0]+txt3[1]

    #Давление
    txt4=all[4].get_text()
    txt4=txt4[0]+txt4[1]+txt4[2]

    #Итог
    itog=[txt1,' ',txt4,' ',txt2,' ',txt3]
    
    return(itog)
#print(get_temp())