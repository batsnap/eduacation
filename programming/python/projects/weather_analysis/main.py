import mail
import rambler
import yandex
import weather
import bbc
import wunderground

a=int(yandex.get_temp())
b=int(rambler.get_temp())
c=int(mail.get_temp())
d=int(weather.get_temp())
g=int(bbc.get_temp())
e=(int(wunderground.get_temp())-32)*(5/9)

print('yandex:',a)
print('rambler:',b)
print('mail:',c)
print('weather:',d)
print('bbc:',g)
print('wunderground:',e)
print('Средняя температура после долгого анализа:',str((a+b+c+d+g)/5))
