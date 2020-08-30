import sqlite3
from sqlite3 import dbapi2
from constants import *

conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.execute("SELECT * FROM hours;")

select_hours = cur.fetchall()

print(['Hours', 'Date Worked', 'Date Of Entry', 'Time Of Entry'])
for row in select_hours:
	print(row)
