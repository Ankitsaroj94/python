import sqlite3

connect = sqlite3.connect("customer.db")

cursor = connect.cursor()


print("--- Order By Row ID Ascending ---")
cursor.execute("SELECT rowid, * FROM customers ORDER BY rowid ASC")
items = cursor.fetchall()
for item in items:
    print(item)

print("--- Order By Row ID Descending ---")
cursor.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
items = cursor.fetchall()
for item in items:
    print(item)

print("\n--- Order By Last Name Alphabetical (ASC) ---")
cursor.execute("SELECT rowid, * FROM customers ORDER BY last_name")

items = cursor.fetchall()
for item in items:
    print(item)

print("\n--- Order By Last Name Des ---")
cursor.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")

items = cursor.fetchall()
for item in items:
    print(item)


connect.commit()
connect.close()
