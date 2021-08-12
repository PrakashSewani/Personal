import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor=mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase") for creating database

"""
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x) well samaj ja
"""

#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

"""
sql="INSERT INTO customers (name,address) VALUES (%s,%s)"
val=[
    ("Dark","Highway 21"),
    ("David","Highway 21"),
    ("Lee","Highway 21"),
    ("Bruce","Highway 21"),
    ("Wayne","Highway 21"),
    ("Kent","Highway 21")
]
mycursor.executemany(sql,val)

mydb.commit()

print(mycursor.rowcount,"Record Inserted")
For Content Insertion
"""

"""
mycursor.execute("SELECT * FROM customers")
myresult=mycursor.fetchall()

for x in myresult:
    print(x)
"""

"""
sql="DROP TABLE IF EXISTS customers"
mycursor.execute(sql)
"""