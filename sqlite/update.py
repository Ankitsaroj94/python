import sqlite3

connect = sqlite3.connect("customer.db")

cursor = connect.cursor()


cursor.execute("""

UPDATE customers SET  first_name ='Change Name'
               WHERE last_name = 'yadav'

""")
connect.commit()
cursor.execute("""

UPDATE customers SET  first_name ='Ankit'
               WHERE rowid = 1

""")
connect.commit()

cursor.execute("SELECT rowid,* FROM customers")

items = cursor.fetchall()
for item in items:
    print(item)


connect.commit()
connect.close()
