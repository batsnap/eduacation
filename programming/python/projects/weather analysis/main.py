import mail
import rambler
import yandex

a=int(yandex.main())
b=int(rambler.main())
c=int(mail.main())
print('Средняя температура после долгого анализа:',str((a+b+c)/3))
