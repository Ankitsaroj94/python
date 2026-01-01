import sqlite3

connect = sqlite3.connect("customer.db")

cursor = connect.cursor()

# create a table

# cursor.execute("""
# CREATE TABLE customers1(
#     first_name text,
#     last_name text,
#     email text
# )""")

# cursor.execute("CREATE TABLE customers( first_name text,last_name text,email text)")


# DataTypes

# NULL
# INTEGER (numbers)
# REAL (decimals)
# TEXT
# BLOB (stored as it is , image , mp3 etc )

# Insert data in table

# cursor.execute("INSERT INTO customers1 VALUES ('Test 2','yadav','test2@test.com')")


# Insert Many data

# many_cust = [
#     (
#         'test1', 'test1', 'test1@test.com'
#     ),
#     (
#         'test2', 'test2', 'test2@test.com'
#     ),
#     (
#         'test3', 'test3', 'test3@test.com'
#     ),
#     (
#         'test4', 'test4', 'test4@test.com'
#     )

# ]

# cursor.executemany("INSERT INTO customers1 VALUES (?,?,?)", many_cust)

# print("Data inserted successfully")

# Quary the Database

cursor.execute("SELECT * FROM customers1")
# print(cursor.fetchmany(2))
# print(cursor.fetchall())


items = cursor.fetchall()

# print("NAME"+"\t\t"+"LASTNAME"+"\t\t"+"EMAIL")
# for item in items:
#     print(item[0] + "\t\t" + item[1] + "\t\t" + item[2])


# print("Data fetched successfully")

# Primary key id

# unique id num in db of items


connect.commit()

connect.close()
