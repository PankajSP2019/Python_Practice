import mysql.connector as db

mydb = db.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="das"
)

mycursor = mydb.cursor()

"""
# Single User input


nm = input("Enter Your Name : ")
sal = input("Enter Your Salary : ")

query = "INSERT INTO employee(name, salary) VALUES(%s, %s)"
values = (nm, sal)

mycursor.execute(query, values)
"""

# Multiple User Input

value_list = list()

n = int(input("How many Data You want To add : "))

for i in range(n):
    value_tuple = list()
    nm = input(f"{i + 1}          Enter Employee Name : ")
    value_tuple.append(nm)
    sal = int(input(f"{i + 1}          Enter Salary of {nm} : "))
    value_tuple.append(sal)
    value_list.append(tuple(value_tuple))
    print("====================================================================")

query = "INSERT INTO employee(name, salary) VALUES(%s, %s)"
values = value_list

mycursor.executemany(query, values)

mydb.commit()

print(mycursor.rowcount, "Record Inserted Successfully")
