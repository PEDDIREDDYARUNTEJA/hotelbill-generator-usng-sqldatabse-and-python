import os
import sqlite3 as sql
con=sql.connect('restaurent')
print("connection established")
curs=con.cursor()
q="create table hotel(itemid int primary key,itemname varchar(10),cost float)"
curs.execute(q)
print("table created")
con.close()