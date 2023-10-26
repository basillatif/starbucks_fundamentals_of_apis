import sqlite3
conn = sqlite3.connect("coffee.db")
coffee = [
    "1, 'Latte', 'Whole', '2022-11-08 09:15:10'",
    "2, 'Cappuccino', 'Oat', '2022-11-08 09:15:13'",
    "3, 'Espresso', 'None', '2022-11-08 09:15:27'",
]
for coffee_data in coffee:
    insert_cmd = f"INSERT INTO coffee VALUES ({coffee_data})"
    conn.execute(insert_cmd)

conn.commit()