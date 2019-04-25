import ui
from random import randit
from time import time
#Глобальные переменные
time1=0
time2=0
primer=0
x=0
osh=0
znaki=['-','+','*']
#подключаемся к базе данных
con = lite.connect('./rez.sqlite')
cur = con.cursor()    
#запуск тренировки/кнопка старт
def start(sender):
   global primer,time1,x
   time1=time()
   primer=str(randit(-100,100))+znaki[randit(0,2)]+str(randit(-100,100))
   lable=sneder.superview['lable1']
   lable.text=primer
#Кнопка следующий пример и отправка ответа
def next(sender):
   global primer,time2,x,osh
   otvet=sneder.superview['textfield1']
   lable=sneder.superview['lable1']
   if x!=5:
      x+=1
      if int(otvet)!=eval(primer):
         osh+=1
      otvet.text=''
      primer=str(randit(-100,100))+znaki[randit(0,2)]+str(randit(-100,100))
      lable.text=primer
   else:
      time2=time()

v = ui.load_view()
v.present('sheet')
