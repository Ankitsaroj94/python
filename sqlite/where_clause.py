import sqlite3

# Connect to the database file 'customer.db'
connect = sqlite3.connect("customer.db")

# Create a cursor object to execute SQL commands
cursor = connect.cursor()

# Execute a SQL query using the WHERE clause to filter records
# This selects all columns (*) where the 'last_name' starts with 'ya'
# The '%' symbol is a wildcard that matches zero or more characters
cursor.execute("SELECT * FROM customers WHERE last_name='Saroj'")

# Fetch all rows that match the query and print them
cursor.execute("SELECT * FROM customers WHERE last_name LIKE 'ya%'")

# Fetch all rows that match the query and print them
items = cursor.fetchall()
for item in items:
    print(item)

# Commit the transaction (saves changes, though none made here) and close the connection
connect.commit()
connect.close()
