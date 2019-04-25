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

x=0
r=0
for i in a.keys():
  newlist.append(i)
def start(sender):
	global x,r
	label = sender.superview['label1']
	label2 = sender.superview['label2']
	if x==0:
		x=1
    rows=row[c]
		label.text=rows[0]
	else:
		x=0
		r=0
		label.text='Слова'
		label2.text='Ошибки'
def but(sender):
	global c,r
	t=sender.title
	label = sender.superview['label1']
	label2 = sender.superview['label2']
	if x==0:
		pass
	else:
		if t==rows[1]
			c=randint(0,184)
      rows=row[c]
			label.text=rows[0]
		else:
			r+=1
			label2.text='Ошибки'+str(r)

v = ui.load_view()
v.present('sheet')
