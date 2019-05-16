# -*- coding: utf-8 -*-
import sqlite3
conn = sqlite3.connect('./my.sqlite')
c = conn.cursor()
try:
   c.execute('CREATE TABLE PrePri (Words TEXT,Letters TEXT)')
except:
   pass
l=[]
a=''
while a!='0':
	try:
		if a!=0:
			a,b=map(str,input().split())
			l.append(a)
			l.append(b)
			c.execute('INSERT INTO PrePri VALUES(?,?)',l)
			l=[]
	except:
		pass
conn.commit()
c.close()
conn.close()
