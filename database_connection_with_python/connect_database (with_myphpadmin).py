# DataBase connect with Python
# Myphpadmin
# All are same as MySQL , difference in connection code

import MySQLdb as db

mydb = db.connect("localhost", "root", "", "onlinefoodshop")  # Connection code

mycursor = mydb.cursor()

query = "select * from customer"

mycursor.execute(query)

mydb.commit()

"""
for i in mycursor:
    print(i)
"""
result = mycursor.fetchall()

for i in result:
    print(i)
