import sqlite3

conn = sqlite3.connect("coffee.db")
columns = [
	"id INTEGER PRIMARY KEY",
	"coffee_name VARCHAR UNIQUE",
	"milk VARCHAR",
	"timestamp DATETIME",
]

create_table_cmd = f"CREATE TABLE coffee ({','.join(columns)})"
conn.execute(create_table_cmd)