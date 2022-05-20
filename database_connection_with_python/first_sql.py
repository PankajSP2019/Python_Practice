"""
from datacame

## Connecting to the database

## importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host="localhost",
    user="root",
    passwd="1234"
)

print(db)  # it will print a connection object if everything is fine
"""

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="das"

)


"""
# Show All Data base name
mycursor = mydb.cursor()
mycursor.execute("show databases")

for i in mycursor:
    print(i)
"""

'''
# Fetch data from database table
mycursor = mydb.cursor()
mycursor.execute("select * from student")

for i in mycursor:
    print(i)
'''

"""
# Fetch data from database table (2nd option and one data from the table)
mycursor = mydb.cursor()
mycursor.execute("select * from student")

result = mycursor.fetchone()
print(result)
for i in result:
    print(i)
"""

# Fetch data from database table (2nd option)
mycursor = mydb.cursor()
mycursor.execute("select * from student")

result = mycursor.fetchall()
result2 = list()

print(result)
for i in result:
    i = list(i)
    result2.append(i)
    print(i)

print(f"new : {result2}")









