import sqlite3

conn=sqlite3.connect("database.db")
print("Open database successfully")

conn.execute("CREATE TABLE employee(name TEXT, addr TEXT, city TEXT, pin TEXT)")

print("Table created successfully")

conn.close()