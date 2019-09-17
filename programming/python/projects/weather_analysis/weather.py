import requests
from bs4 import BeautifulSoup

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
    chifri='0123456789'
    temp=soup.select('div.today_nowcard-temp')
    txt1=temp[0].get_text()
    s=''
    for i in range(len(txt1)):
        if txt1[i] in chifri:
            s+=txt1[i]
    txt1=s

    #Влажность
    all=soup.select('span')
    txt2=all[68].get_text()
    txt2=txt2[0]+txt2[1]

    #Давление
    txt3=all[72].get_text()
    txt33=''
    for i in range(len(txt3)):
        if txt3[i] in chifri:
            txt33+=txt3[i]
        if txt3[i]==',':
            txt33+='.'
    txt3=txt33
    txt3=str(float(txt3)*0.750062)

    #Ветер
    cif='0123456789'
    txt41=''
    txt4=all[67].get_text()
    if txt4=='Штиль':
        txt4='0'
    else:
        for i in range(len(txt4)):
            if txt4[i] in cif:
                txt41+=txt4[i]
        txt4=str(float(txt41)/3.2)
    

    #Записываем все в массим для удобства
    itog=[txt1,' ',txt3,' ',txt4,' ',txt2]

    return(itog)
#print(get_temp())