"""
Author : Pankaj Kumar Das
Start Date : 14/05/2022
Purpose : Build a Console baseLibrary Management System with Database and using MYSQL as Database server.
Project Name : Library Management System
"""

import mysql.connector as db
from datetime import datetime


class library:

    def __init__(self):
        self.mydb = db.connect(
            host="localhost",
            user="root",
            passwd="1234",
            database="onlineLibrary"  # database for this project
        )

    # This function is add book in the library by visitors, customer, readers
    def donateBook(self):
        """
        Visitors, customer, readers can add book to the library.
        Donate details will save in donatedetails and bookdetails database table.
        """

        while True:
            try:
                print("...............................................................")
                name = input("Enter Your Name : ")
                mobile = input("Enter Your Mobile Number : ")
                email1 = input("Enter Your Email Address : ")
                date = datetime.now().date()
                status = "Available"
                addBy = name

                print("...............................................................")
                c1 = int(input("How Many Book You want to add : "))
                all_value_list_bookdeatils = list()  # value of this list will add in Book Details
                all_value_list_donatedetails = list()  # value of this list will add in Donate Details
                for i in range(c1):
                    temp1 = list()
                    temp2 = list()
                    print(f"--------------{i + 1}--------------")
                    bookName = input("Enter Book Name : ")
                    author_name = input("Enter Author Name : ")
                    quntity = int(input("How Many Copy(Int value) : "))

                    temp1.extend([bookName, author_name, quntity, status,
                                  addBy])  # extend([]) insert multiple values in a list at a time
                    temp2.extend([bookName, author_name, quntity, name, mobile, email1, date])

                    all_value_list_bookdeatils.append(tuple(temp1))
                    all_value_list_donatedetails.append(tuple(temp2))
                    print(f"---------------------------------")

                # Insert Information int= the donatedetails database table
                mycursor3 = self.mydb.cursor()
                query1 = f"INSERT INTO donatedetails(book_name, author_name, quantity, name, mobile, email, date) VALUES(%s, %s, %s, %s, %s, %s, %s)"
                mycursor3.executemany(query1, all_value_list_donatedetails)
                self.mydb.commit()

                # Insert Information in the bookdetails database table
                mycursor2 = self.mydb.cursor()
                query = f"INSERT INTO bookdetails(book_name, author_name, quatity, status, addBy) VALUES(%s, %s, %s, %s, %s)"
                mycursor2.executemany(query, all_value_list_bookdeatils)
                self.mydb.commit()

                print("...............................................................")
                print(mycursor3.rowcount, "Book Donated Successfully")
                print(f"Thank You {name}")
                print("...............................................................")
                break

            except Exception as e:
                print("...............................................................")
                print(e)
                print("Something is wrong..Try again.")
                h1 = input("Want to Continue ?(Type 0 for YES) : ")
                print("...............................................................")
                if h1 == '0':
                    continue
                else:
                    break

    # End Donate book function

    # This function is add book in the library by Admin
    def addBook(self):
        """
        Added book by admin to the Library. Store the information in the bookdetails database table

        """

        while True:
            try:
                print("...............................................................")
                c1 = int(input("How Many Book You want to add : "))
                all_value_list = list()
                for i in range(c1):
                    status = ""
                    temp = list()
                    print(f"--------------{i + 1}--------------")
                    bookName = input("Enter Book Name : ")
                    author_name = input("Enter Author Name : ")
                    quntity = int(input("How Many Copy(Int value) : "))
                    if quntity > 0:
                        status = "Available"
                    else:
                        status = "Not Available"

                    addBy = "admin"
                    temp.extend([bookName, author_name, quntity, status,
                                 addBy])  # extend([]) insert multiple values in a list at a time
                    all_value_list.append(tuple(temp))
                    print(f"---------------------------------")

                mycursor1 = self.mydb.cursor()
                query = f"INSERT INTO bookdetails(book_name, author_name, quatity, status, addBy) VALUES(%s, %s, %s, %s, %s)"
                mycursor1.executemany(query, all_value_list)
                self.mydb.commit()
                print("...............................................................")
                print(mycursor1.rowcount, "Book Inserted Successfully")
                print("...............................................................")
                break

            except Exception as e:
                print("...............................................................")
                print(e)
                print("Something is wrong..Try again.")
                h1 = input("Want to Continue ?(Type 0 for YES) : ")
                print("...............................................................")
                if h1 == '0':
                    continue
                else:
                    break

    # End Add book function by admin

    def borrowBook(self):
        """
        Customer, Reader, Visitor borrow book from library. 1st customer have entered book id which he/she want to borrow
        Then the system will check if the entered book is available or not in the library. if available then he/she can borrow the
        book. And all the details will save in the borrowdetails database table and a update will occure in quantity/copies of books
        in the available book list , bookdetails database library

        """
        print("You Can Borrow Maximum 5  Books at a time and 1 copies from each book")

        # fetch all information, will need later
        mycursor4 = self.mydb.cursor()
        query = "select * from bookdetails where status = 'Available'"
        mycursor4.execute(query)
        result_bookdetails = mycursor4.fetchall()  # all information of bookdetails table
        result1_bookdetails_id = [i[0] for i in result_bookdetails]  # only the book_id's of bookdetails table in a list

        while True:

            try:
                print("...............................................................")
                C_name = input("Enter Your Name : ")
                mobile = input("Enter Your Mobile Number : ")
                email1 = input("Enter Your Email Address : ")
                b_date = datetime.now().date()
                c2 = int(input("How Many Book want to borrow ?(not more than 5) : "))
                print("...............................................................")

                vaild_book_id_list = list()
                for i in range(c2):
                    print(f"--------------{i + 1}--------------")
                    b_id = int(input("Enter Book ID (INT Number) :"))
                    if b_id in result1_bookdetails_id:
                        vaild_book_id_list.append(b_id)
                    else:
                        print("...............................................................")
                        print("Opps, You Entered Wrong Book ID\nOR the Book is not available right now")
                        print("...............................................................")

            except Exception as e:
                print("...............................................................")
                print(e)
                print("Something is wrong..Try again.")
                h1 = input("Want to Continue ?(Type 0 for YES) : ")
                print("...............................................................")
                if h1 == '0':
                    continue
                else:
                    break


if __name__ == '__main__':
    lib = library()
    lib.borrowBook()
