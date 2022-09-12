"""
Author : Pankaj Kumar Das
Start Date : 14/05/2022
Purpose : Build a Console baseLibrary Management System with Database and using MYSQL as Database server.
Project Name : Library Management System
"""

import mysql.connector as db


class library:


    def donateBook(self):
        pass

    def addBook(self):
        mydb = db.connect(
            host="localhost",
            user="root",
            passwd="1234",
            database="onlineLibrary"  # database for this project
        )
        while True:
            try:
                c1 = int(input("How Many Book You want to add : "))
                all_value_list = list()
                for i in range(c1):
                    temp = list()
                    print(f"--------------{i+1}--------------")
                    bookName = input("Enter Book Name : ")
                    author_name = input("Enter Author Name : ")
                    quntity = int(input("How Many Copy(Int value) : "))
                    status = "Available"
                    temp.extend([bookName, author_name, quntity, status]) # extend([]) insert multiple values in a list at a time
                    all_value_list.append(tuple(temp))
                    print(f"---------------------------------")

                mycursor1 = mydb.cursor()
                query = f"INSERT INTO bookdetails(book_name, author_name, quatity, status) VALUES(%s, %s, %s, %s)"
                mycursor1.executemany(query, all_value_list)
                mydb.commit()
                print(mycursor1.rowcount, "Record Inserted Successfully")
                break

            except Exception as e:
                print(e)
                break # remove later


    def borrowBook(self):
        pass


if __name__ == '__main__':
    lib = library()
    lib.addBook()
