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

c=randint(0,184)
v=[]
x=0
r=0
def start(sender):
	global x,r,v,f,k
	label = sender.superview['label1']
	label2 = sender.superview['label2']
	if x==0:
		x=1
		v=rows[c]
    f=v[0]
    k=v[1]
		label.text=f
	else:
		x=0
		r=0
		label.text='Слова'
		label2.text='Ошибки'
def but(sender):
	global c,r,v,f,k
	t=sender.title
	label = sender.superview['label1']
	label2 = sender.superview['label2']
	if x==0:
		pass
	else:
		if t==k:
			c=randint(0,184)
      v=rows[c]
      f=v[0]
      k=v[1]
			label.text=f
		else:
			r+=1
			label2.text='Ошибки'+str(r)

v = ui.load_view()
v.present('sheet')
