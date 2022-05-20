import mysql.connector as db

mydb = db.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="das"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE employee (name VARCHAR(255), salary INT(11) )") # create table with out primary key
# mycursor.execute("ALTER TABLE employee ADD COLUMN id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST") # create table with primary key


'''

# Inserting Multi Row
query = "INSERT INTO employee(name, salary) VALUES(%s, %s)"
values = [
    ("Rudrika", 100),
    ("korim", 300),
    ("rohim", 500)
]

mycursor.executemany(query, values)

mydb.commit() ## to make final output we have to run the 'commit()' method of the database object

'''

# Inserting Single Row
query = "INSERT INTO employee(name, salary) VALUES(%s, %s)"
values = ("Jonny", 2000)

mycursor.execute(query, values)

mydb.commit()
# result = mycursor.fetchall()
# print(result)

print(mycursor.rowcount,"Record Inserted") # TO Show how many row of the inserted

