import ui
from random import randint
from time import time
import sqlite3 as lite
#Глобальные переменные
time1=0
time2=0
primer=0
x=0
osh=0
znaki=['-','+','*']
rez=[]
#подключаемся к базе данных
con = lite.connect('./rez.sqlite')
cur = con.cursor()    
#запуск тренировки/кнопка старт
def start(sender):
   global primer,time1,x
   time1=time()
   primer='('+str(randint(-100,100))+')'+znaki[randint(0,2)]+'('+str(randint(-100,100))+')'
   lable=sender.superview['label1']
   lable.text=primer
#Кнопка следующий пример и отправка ответа
def next(sender):
   global primer,time2,x,osh,rez
   otvet=sender.superview['textfield1']
   lable=sender.superview['label1']
   lable1=sender.superview['label2']
   if x!=5:
      x+=1
      if otvet!=eval(primer):
         osh+=1
      otvet.text=''
      primer='('+str(randint(-100,100))+')'+znaki[randint(0,2)]+'('+str(randint(-100,100))+')'
      lable.text=primer
   else:
      
      time2=time()
      rez.append(int(time2-time1))
      rez.append(osh)
      lable.text='Пример'
      lable1.text='Ошибки:'+str(osh)
      cursor.execute("INSERT INTO rez VALUES (?,?)", rez)
v = ui.load_view()
v.present('sheet')
