# -*- coding: utf-8 -*-
import sqlite3
conn = sqlite3.connect('./my.sqlite')
c = conn.cursor()
try:
   c.execute('CREATE TABLE PrePri (Words TEXT,Letters TEXT)')
except:
   pass
l=[]
for i in range (185):
   c.execute('INSERT INTO PrePri VALUES(?,?)',l)
   
conn.commit()
c.close()
conn.close()