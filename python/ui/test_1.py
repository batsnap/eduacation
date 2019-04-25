# -*- coding: utf-8 -*-
import ui
from random import randint
import sqlite3 as lite
import sys
i=1
con = lite.connect('./my.sqlite')

with con:    
  cur = con.cursor()    
  cur.execute("SELECT * FROM PrePri")
  rows = cur.fetchall()
a=[]
b=[]
for row in rows:
  a.append(row[0])
  b.append(row[1])
c=randint(0,184)
v=[]
x=0
r=0
def start(sender):
	global x,r
	label = sender.superview['label1']
	label2 = sender.superview['label2']
	if x==0:
		x=1
		label.text=a[c]
	else:
		x=0
		r=0
		label.text='Слова'
		label2.text='Ошибки'
def but(sender):
	global c,r,x
	t=sender.title
	label = sender.superview['label1']
	label2 = sender.superview['label2']
	if x==0:
		pass
	else:
		if t==b[c]:
			c=randint(0,184)
			label.text=a[c]
		else:
			r+=1
			label2.text='Ошибки'+str(r)

v = ui.load_view()
v.present('sheet')
