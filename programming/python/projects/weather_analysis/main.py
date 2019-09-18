import rambler, yandex,weather,bbc, wunderground,mail

def weatherbot():
    a=yandex.get_temp()
    b=rambler.get_temp()
    c=mail.get_temp()
    d=weather.get_temp()
    g=bbc.get_temp()
    e=(int(wunderground.get_temp())-32)*(5/9)

    #Температура
    ItogTemp='Температура после долгого анализа:'+str((int(a[0])+int(b[0])+int(c[0])+int(d[0])+int(g[0])+e)/6)

    #Давление
    ItogBar='Давление после долгого анализа:'+str((int(a[2])+int(b[2])+int(c[2])+float(d[2])+float(g[2]))/5)

    #Скорость ветра
    #https://meteoinfo.ru/bofort
    ItogWind='Скорость ветра после долгого анализа:'+str((float(a[4])+int(b[4])+float(c[4])+float(d[4])+float(g[4]))/5)

    #Влажность
    ItogWet='Влажнность после долгого анализа:'+str((float(a[6])+float(c[6])+float(d[6])+float(g[6]))/4)

    return ItogTemp+'\n'+ItogBar+'\n'+ItogWind+'\n'+ItogWet
#print(weatherbot()) 