import sqlite3
import csv
from sqlite3 import dbapi2
from datetime import date
from constants import *

conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.execute("SELECT hours FROM hours;")

select_hours = cur.fetchall()
total_hours = 0
for row in select_hours:
	total_hours += float('{0}'.format(row[0]))

pay = total_hours * WAGE
print("Total hours: ",total_hours)
print("Pay for this period: £",pay)

def write_csv():
	print("Writing CSV...")
	today = date.today()
	write_date_as_filename = today.strftime("%d.%m.%y") + ".csv"
	get_data = cur.execute("SELECT * FROM hours;")
	with open(write_date_as_filename, "w", newline='') as csv_file:
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow(['Total Pay: ', pay, '', ''])
		csv_writer.writerow(['Hours', 'Date Worked', 'Date Of Entry', 'Time Of Entry'])
		for i in get_data:
			csv_writer.writerow(i)
			csv_writer.writerows(cur)

def wipe_db():
	print("Deleting table...")
	cur.execute("DELETE FROM hours;")
	conn.commit()
	conn.close()

def end_pay_period_confirm(answer):
	print("Are you sure? (Y/N)")
	answer = input()
	if answer == "Y":	
		write_csv()
		wipe_db()
		quit()
	elif answer == "N":
		quit()
	else:
		end_pay_period_confirm(answer)

def end_pay_period():
	print("End pay period? (Y/N)")
	answer = input()
	if answer == "Y":
		end_pay_period_confirm(answer)
	elif answer == "N":
		quit()
	else:
		end_pay_period()

end_pay_period()
