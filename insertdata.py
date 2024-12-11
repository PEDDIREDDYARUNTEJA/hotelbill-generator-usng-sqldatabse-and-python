import os
import sqlite3 as sql
con=sql.connect("restaurent")
print("connection established")
curs=con.cursor()
q="insert into hotel values(1,'idli',50.0),(2,'pesarattu',70.0),(3,'parota',55.0),(4,'upma',40.0),(5,'puri',45.0),(6,'chapati',30.0),(7,'dosa',45.0),(8,'bonda',60.0)"
curs.execute(q)
con.commit()
print("data inserted in the table")
con.close()
