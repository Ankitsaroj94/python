import sqlite3

connect = sqlite3.connect("customer.db")

cursor = connect.cursor()
cursor.execute("SELECT rowid,* FROM customers")
items = cursor.fetchall()
for item in items:
    print(item)


connect.commit()
connect.close()
