import mail
import rambler
import yandex
import weather

a=int(yandex.main())
b=int(rambler.main())
c=int(mail.main())
d=int(weather.main())
print('yandex:',a)
print('rambler:',b)
print('mail:',c)
print('weather:',d)
print('Средняя температура после долгого анализа:',str((a+b+c+d)/4))
