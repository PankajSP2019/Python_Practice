"""
Author : Pankaj Kumar Das
Date : 14/05/2022
Purpose : Database CRUD operation
Problem Name : SQL_CURD
"""

import mysql.connector as db

host_name = ""
user_name = ""
password = ""
data_base = ""


# Function for Insert Data into
def insert_data(db_object):
    mycursor = db_object.cursor()
    table_name = input("Enter table name : ")
    query = f"DESC {table_name}"  # all information of table
    mycursor.execute(query)
    result = mycursor.fetchall()  # all information of table store in this variable

    print(result)
    column_name_list = list()  # will store all cloumn name of table
    value_list = list()  # will store values(user input) which user want to insert to database table

    for i in result:
        if 'auto_increment' not in i:  # auto_increment will add automatically in the column
            column_name_list.append(i[0])  # add column name into list
            aaa = input(f"Enter {i[0]} : ")  # user input for column's value
            value_list.append(aaa)  # add user input into list

    # column_name_tuple = tuple(column_name_list)

    column_names = ",".join(column_name_list)  # convert column name's list in string with ","

    # Insert into table
    query1 = f"INSERT INTO {table_name}({column_names}) VALUES(%s, %s)"
    values1 = tuple(value_list)
    mycursor.execute(query1, values1)
    db_object.commit()
    print(mycursor.rowcount, "records inserted")

    # for Insert again
    print("\n=================================================================\n")
    aa = input("Do you want to Insert Data agian ?(type y for yes)) : ")
    if aa == "y":
        insert_data(db_object)
    else:
        print("=================================================================")
        # exit("Thanks For using me !!")

    # result = mycursor.fetchall()
    # print(result)


# end insert function

# Function for Delete Data from database
def delete_data(db_object):
    mycursor = db_object.cursor()
    table_name = input("Enter table name : ")
    query = f"DESC {table_name}"  # all information of table
    mycursor.execute(query)
    result = mycursor.fetchall()  # all information of table store in this variable

    print(result)  # print all information of table

    print("---------------------------------------------------------------------------------")
    print("You Want Delete Data By : ")
    cc = 1
    for i in result:
        print(f"{cc}. {i[0]}    ", end="")
        cc = cc + 1
    ccc = input(f"| Enter your choose by pressing 1 to {cc - 1} : ")  # Input for
    print("\n---------------------------------------------------------------------------------")

    column_name = ""  # Declear and initialize column name
    which_delete = ""  # input("Name Want TO DELETE : ")

    while True:
        if int(ccc) <= len(result):
            column_name = result[int(ccc) - 1][0]
            # print("---------------------------------------------------------------------------------")
            break
        else:
            print("---------------------------------------------------------------------------------")
            print(f"You Entered Wrong Number.....!!")
            in_again = input("Do You Want to Enter Again ?(Type y for Yes) : ")
            if in_again == "y":
                print("*********************************************************************************")
                cc = 1
                for i in result:
                    print(f"{cc}. {i[0]}    ", end="")
                    cc = cc + 1
                ccc = input(f"| Enter your choose by pressing 1 to {cc - 1} : ")
                print("*********************************************************************************")
                continue
            else:
                print("---------------------------------------------------------------------------------")
                break
    print("\n----------------------------------")
    print(f"| You Select {column_name} |")
    print("----------------------------------")

    print("\n.....................................................................................")
    which_delete = input(f"Which Record You Want To Delete From {column_name}, Enter The value : ")
    print(".....................................................................................")

    query1 = f"DELETE FROM {table_name} WHERE {column_name} = '{which_delete}' "  # Delete Query
    mycursor.execute(query1)
    db_object.commit()

    if mycursor.rowcount == 0:
        print(f"OPps!!!.It seems like you entered wrong value...\nWhich not in '{column_name}' column.")
        print("....................................")
        print(mycursor.rowcount, "Row Effected")
        print("....................................")
    else:
        print("....................................")
        print(mycursor.rowcount, "Record Deleted Successfully")
        print("....................................")

    # for Delete again
    print("\n=================================================================\n")
    aa = input("Do you want to Delete Data again ?(type y for yes)) : ")
    if aa == "y":
        delete_data(db_object)
    else:
        print("=================================================================")

# end delete function


print("----------------------------------------------------------------------------------")
a = input("Do you want to connect with MySQL Server(type y for yes) : ")
print("----------------------------------------------------------------------------------")

if a == "y":
    host_name = input("Enter host Name : ")
    user_name = input("Enter user Name : ")
    password = input("Enter Password : ")
    data_base = input("Enter Specific Database Name : ")
else:
    print("Thanks For Being With us !!!!!")
    exit("Have a good day!!!!")

try:

    mydb = db.connect(
        host=host_name,
        user=user_name,
        passwd=password,
        database=data_base
    )
    print("----------------------------------------------------------------------------------")
    print("Successfully Connected..!!!")
    print("----------------------------------------------------------------------------------")
    print("\n\n")

    while True:
        print("----------------------------------------------------------------------------------------------------------------------")
        print("1.Insert Data   2.Delete Data   3.Read Data   4.Update Data   5.Exit ", end="|")
        st = input(" What Do You Want To Do, Insert (1 to 5) : ")
        print("\n---------------------------------------------------------------------------------------------------------------------")
        if st == "1":
            insert_data(mydb)
        elif st == "2":
            delete_data(mydb)
        elif st == "3":
            print("Not Yet Developed")
        elif st == "4":
            print("Not Yet Developed")
        elif st == "5":
            print("Thank You ")
            break
        else:
            print(".....................................................")
            print("It seems you entered wrong value\nPlease try Again..!")
            print(".....................................................")
            continue

except Exception as e:
    print("----------------------------------------------------------------------------------")
    print("Opps...Connection Not Successful!!!!")
    print(e)
    print("----------------------------------------------------------------------------------")
