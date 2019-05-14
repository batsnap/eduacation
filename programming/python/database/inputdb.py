# -*- coding: utf-8 -*-
import sqlite3
conn = sqlite3.connect('./rez.sqlite')
c = conn.cursor()
c.execute('CREATE TABLE rez (Time REAL ,osh INTEGER)')

   
conn.commit()
c.close()
conn.close()