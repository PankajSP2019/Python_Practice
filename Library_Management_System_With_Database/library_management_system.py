"""
Author : Pankaj Kumar Das
Start Date : 14/05/2022
Purpose : Build a Console baseLibrary Management System with Database and using MYSQL as Database server.
Project Name : Library Management System
"""

"""
Work list

Next work is - At a time if the quantity of a book becomes 0 then the status of the book will automatically
changed(updated)  to Not Available in the database.

"""

"""
start work 30/01-2023
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
        query = "select book_id,book_name,author_name,quatity from bookdetails where status = 'Available'"
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

                print("...............................................................")
                # a feature, a customer identify by his/her mobile number
                # if he/she already borrow 5 books he can not borrow more books
                # he/she have to return pervious borrow
                # collect mobile from borrowdetails table then identify by count() function
                # if count("mobile_number") > 5 , cannot borrowbook

                valid_borrow_book_id_list = list()
                valid_borrow_book_name_list = list()
                valid_borrow_book_quantity_list = list()
                book_id_and_book_name = list()
                while True:
                    print("...............................................................")
                    c2 = int(input("How Many Book want to borrow ?(not more than 5) : "))
                    if 5 >= c2 > 0:
                        for i in range(c2):
                            print(f"--------------{i + 1}--------------")
                            b_id = int(input("Enter Book ID (INT Number) :"))
                            if (b_id in result1_bookdetails_id) and (b_id not in valid_borrow_book_id_list):
                                valid_borrow_book_id_list.append(b_id)
                                # store valid and borrowed book names in a list
                                for k in result_bookdetails:
                                    if b_id == k[0]:
                                        valid_borrow_book_name_list.append(k[1])
                                        valid_borrow_book_quantity_list.append(k[3])
                            else:
                                print("...............................................................")
                                print(
                                    "Opps, You Entered Wrong Book ID\nOR the Book is not available right now\nAlready Entered this ID")
                                print("...............................................................")
                        # show selected books
                        from prettytable import PrettyTable
                        t = PrettyTable(["BOOK_ID", "BOOK_NAME", "AUTHOR_NAME", "AVAILABLE_COPIES"])
                        for i in valid_borrow_book_id_list:
                            for j in result_bookdetails:
                                if i == j[0]:
                                    t.add_row(j)
                        print("You Select : ")
                        print(t)

                        book_id_and_book_name_and_quantity = zip(valid_borrow_book_id_list, valid_borrow_book_name_list,
                                                                 valid_borrow_book_quantity_list)
                        # book_id_and_book_name = ((ID, BOOK_NAME, QUANTITY))

                        # next work will in here
                        # database query implementation
                        for k in book_id_and_book_name_and_quantity:
                            mycursor5 = self.mydb.cursor()
                            query = f"INSERT INTO borrowdetails(book_id, book_name, borrow_date, customer_name, mobile, email) VALUES({k[0]} , '{k[1]}' , '{b_date}' , '{C_name}' , '{mobile}' , '{email1}')"
                            mycursor5.execute(query)
                            self.mydb.commit()

                            mycursor6 = self.mydb.cursor()
                            query = f"UPDATE bookdetails SET quatity = {k[2] - 1} WHERE book_id = {k[0]}"
                            mycursor6.execute(query)
                            self.mydb.commit()

                        print("...............................................................")
                        print("Successfully Borrowed\nThanks for being with us")
                        print("...............................................................")
                        break


                    else:
                        print("...............................................................")
                        print("Wrong Input\nPlease try again\nYou can not borrow more than 5 books")
                        h2 = input("Want to Continue ?(Type 0 for YES) : ")
                        print("...............................................................")
                        if h2 == '0':
                            continue
                        else:
                            break

                """print(valid_borrow_book_id_list)
                print(valid_borrow_book_name_list)
                print(list(book_id_and_book_name))"""
                break  # main loop

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
