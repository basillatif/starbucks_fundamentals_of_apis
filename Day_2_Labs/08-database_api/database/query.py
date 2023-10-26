import sqlite3
conn = sqlite3.connect("coffee.db")
cur = conn.cursor()

cur.execute("SELECT * FROM coffee")


coffee = cur.fetchall()
for c in coffee:
	print(c)