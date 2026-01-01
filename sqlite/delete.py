import sqlite3

connect = sqlite3.connect("customer.db")

cursor = connect.cursor()


cursor.execute("""

DELETE from customers1 WHERE last_name='Saroj'

""")
connect.commit()


cursor.execute("SELECT rowid,* FROM customers")

items = cursor.fetchall()
for item in items:
    print(item)


connect.commit()
connect.close()


# import sqlite3

# connect = sqlite3.connect("customer.db")

# cursor = connect.cursor()


# cursor.execute("""

# DELETE from customers1 WHERE email LIKE '%test.com'

# """)
# connect.commit()


# cursor.execute("SELECT rowid,* FROM customers1")

# items = cursor.fetchall()
# for item in items:
#     print(item)


# connect.commit()
# connect.close()
