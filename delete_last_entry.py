import sqlite3
from sqlite3 import dbapi2
from constants import *

conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.execute("DELETE FROM hours WHERE rowid = (SELECT MAX(rowid) FROM hours);")
conn.commit()
conn.close()

print("Most recent entry deleted...")
import total_hours
