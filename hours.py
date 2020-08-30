import time
import sqlite3
from sqlite3 import dbapi2
from datetime import date
from constants import *

date_entered = time.strftime("%d, %m, %y")
time_entered = time.strftime("%H, %M, %S")

def get_hours():
	hours = input("Enter hours: ")
	try:
		return float(hours)
	except ValueError:
		return get_hours()

def get_date():
	date_worked = input("Enter date worked: ")
	if not date_worked:
		date_worked = time.strftime("%d, %m, %y")
	return date_worked

hours = get_hours()
date_worked = get_date()

insert = [(hours, date_worked, date_entered, time_entered)
	]

conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.executemany("INSERT INTO hours VALUES (?, ?, ?, ?)", insert)
conn.commit()

import total_hours
