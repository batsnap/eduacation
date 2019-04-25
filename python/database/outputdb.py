# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys
i=1
con = lite.connect('./my.sqlite')
 
with con:    
   cur = con.cursor()    
   cur.execute("SELECT * FROM PrePri")
   rows = cur.fetchall()

   for row in rows:
      print (i,':',row)
      i+=1