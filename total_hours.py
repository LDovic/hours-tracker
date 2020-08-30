import sqlite3
import csv
from sqlite3 import dbapi2
from datetime import date
from constants import *

conn = sqlite3.connect("hours.db")
cur = conn.cursor()
cur.execute("SELECT hours FROM hours;")

select_hours = cur.fetchall()
total_hours = 0
for row in select_hours:
	total_hours += float('{0}'.format(row[0]))

pay = total_hours * WAGE
print("Pay for this period: £",pay)
