import mysql.connector as db

# host_name = input("Enter host Name : ")
# user_name = input("Enter user Name : ")
# password = input("Enter Password : ")
# data_base = input("Enter Specific Database Name : ")

mydb = db.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="das")

table_name = "employee"
nm = "pkpk"
sal = 10012
mycursor = mydb.cursor()

# query = f"INSERT INTO {table_name}(name, salary) VALUES(%s, %s)" # its also work
query = "INSERT INTO " + table_name + "(name, salary) VALUES(%s, %s)"

values = (nm, sal)
mycursor.execute(query, values)
mydb.commit()

print(mycursor.rowcount, "INSERT SUCCESSFULLY")
mydb.close()
