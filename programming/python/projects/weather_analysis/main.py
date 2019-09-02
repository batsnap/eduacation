import rambler, yandex,weather,bbc, wunderground,mail

#Прием данных из подпрограмм
a=yandex.get_temp()
b=rambler.get_temp()
c=mail.get_temp()
d=weather.get_temp()
g=bbc.get_temp()
e=(int(wunderground.get_temp())-32)*(5/9)

#Температура
ItogTemp=(int(a[0])+int(b[0])+int(c[0])+int(d[0])+int(g[0])+e)/6
print('Температура после долгого анализа:',ItogTemp)

#Давление
ItogBar=(int(a[2])+int(b[2])+int(c[2])+float(d[2])+float(g[2]))/5
print('Давление после долгого анализа:',ItogBar)

#Скорость ветра
#https://meteoinfo.ru/bofort
ItogWind=(float(a[4])+int(b[4])+float(c[4])+float(d[4])+float(g[4]))/5
print('Скорость ветра после долгого анализа:',ItogWind)

#Влажность
ItogWet=(float(a[6])+float(c[6])+float(d[6])+float(g[6]))/4
print('Влажнность после долгого анализа:',ItogWet)