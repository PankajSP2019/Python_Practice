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

    # print(result)
    column_name_list = list()  # will store all cloumn name of table
    value_list = list()  # will store values(user input) which user want to insert to database table
    value_query_list = list()  # for query write , how many value with insert (%s)
    for i in result:
        if 'auto_increment' not in i:  # auto_increment will add automatically in the column
            column_name_list.append(i[0])  # add column name into list
            aaa = input(f"Enter {i[0]} : ")  # user input for column's value
            value_list.append(aaa)  # add user input into list
            value_query_list.append("%s")  # add %s in a list , it needed to write query for insert value

    # column_name_tuple = tuple(column_name_list)

    column_names = ",".join(column_name_list)  # convert column name's list in string with ","
    value_s_list_query = ",".join(value_query_list)  # convert %s's list in string with "," , we need this to insert value

    # Insert into table
    query1 = f"INSERT INTO {table_name}({column_names}) VALUES({value_s_list_query})"
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

    # print(result)  # print all information of table

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


# Read Function

def read_op(mydb):
    """# here have many print data style
    # https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data


    # PrettyTable: https://pypi.python.org/pypi/PrettyTable
    from prettytable import PrettyTable
    t = PrettyTable(['Name', 'Age'])
    t.add_row(['Alice', 24])
    t.add_row(['Bob', 19])
        print(t)

    # tabulate
    from tabulate import tabulate
    print(tabulate(result)) # result is a list
    # print(tabulate([['Alice', 24], ['Bob', 19]], headers=['Name', 'Age'], tablefmt='orgtbl'))"""

    table_field_name = list()  # name of fields of selected table, will store in this list for printing purpose
    print("-------------------------------------------------------")
    table_nm = input("Enter Table Name : ")
    print("-------------------------------------------------------")

    print(f"\n                Showing All Data Of Table ({table_nm})\n")

    # Information of Table
    mycursor1 = mydb.cursor()
    query1 = f"DESC {table_nm}"
    mycursor1.execute(query1)
    result1 = mycursor1.fetchall()
    # print(result1) # for check

    # all the table field name store in a list
    for i in result1:
        table_field_name.append(i[0])

    # print(table_field_name) # for checking

    # Data of table
    mycursor = mydb.cursor()
    query = f"SELECT * FROM {table_nm}"
    mycursor.execute(query)
    result = mycursor.fetchall()
    # print(result) # for check

    # print all the information of table using, PrettyTable, a python module
    from prettytable import PrettyTable
    t = PrettyTable(table_field_name)
    for i in result:
        t.add_row(i)
    print(t)


# End Read Function

# Update Function
# It will update specific value , by the help of primary key

def update_op(mydb):
    # update method

    mycursor = mydb.cursor()
    table_name = input("Enter table name : ")
    query = f"DESC {table_name}"  # all information of table
    mycursor.execute(query)
    result = mycursor.fetchall()  # all information of table store in this variable

    # print(result) # print all information of table

    mycursor1 = mydb.cursor()
    query1 = f"SELECT * FROM {table_name}"  # all the data of the table
    mycursor1.execute(query1)
    result1 = mycursor1.fetchall()  # all data of the table store in this variable
    # print(result1) # print all data of the table

    # We will update the values, regarding id number or primary number.

    primary_field = ""  # we are going to update regarding primary number, and primary field name will store in this variable and use this in query.
    count11 = 0
    k = 0  # for find the location value of primary number
    primary_field_position = int()
    for i in result:
        if i[3] == "PRI":
            primary_field = i[0]
            primary_field_position = k
            print("Primary Field Selected..")
            count11 = count11 + 1
        k = k + 1

    # print(f"Primary Key position {primary_field_position}") #print the position of primary key field in table.

    """
    # not need now
    if count11 == 0 :
        print("There is no Primary Field...")
        # here have to write some code , if primary field not found 
        # then the user can not continue the system or break the system
    """

    if primary_field:
        print("\n...................................................................................")
        print(
            f"System Detect that PRIMARY KEY of table ({table_name}) is ({primary_field})\nYou Have Updateed By Primary Key value")
        # primary_value = "" # This is primary key value , we have to updated value by this, and assum that this value in INT
        print("...................................................................................\n")

    # main loop
    while True:  # 1111 theke ai loop er agge porjonto sob ai loop er vitor dhukabo, next task

        if (not primary_field):
            print("\n...................................................................................")
            print("There is no Primary Key field in the entered table.\nYou cannot update without Primary key.")
            print("\n...................................................................................")
            break

        print("---------------------------------------------------------------------------------")
        primary_value = int(input(
            f"Enter ({primary_field}), Where you wanted to Update ({result[primary_field_position][1]} value) :  "))
        print("---------------------------------------------------------------------------------")
        # Check weather the entered primary key is in the database or not
        m = 0  # for count
        for i in result1:
            for j in i:
                if primary_value == j:
                    print(f"{primary_value} : Your Entered ({primary_field}) is Found in DATABASE.")
                    m = m + 1
                    # break

        if m == 0:
            print(f"{primary_value} :Your Entered ({primary_field}) is NOT Found in DATABASE.")
            # exit("hi i am exiting")  # please remove it later
            oo = input("Do you want to continue Updating ? (press 0 for YES) : ")
            if oo == '0':
                continue
            else:
                break

        # Where user want to update
        print("You Want To Update IN : ")
        cc = 0
        list_dummy = list()  # store the values(addresss), with out primary number address
        for i in result:
            # DONE --> have to change here, that primary or auto increment fields are not available for update, we cant update primary or auto increment value;
            # [('id', b'int', 'NO', 'PRI', None, 'auto_increment')] --> primary number serial is  tuple[3]
            if i[3] != "PRI":
                list_dummy.append(cc)
                print(f"{cc}. {i[0]}    ", end="")
            cc = cc + 1
        ccc = input(f"| Enter your choose by pressing Number : ")  # Input for
        print("\n---------------------------------------------------------------------------------")

        # print(list_dummy) # just for check

        column_name = ""  # Declear and initialize column name
        which_delete = ""  # input("Name Want TO DELETE : ")

        if (int(ccc) <= len(result)) and (int(ccc) in list_dummy):
            column_name = result[int(ccc)][0]
            # print(f"-----------------------------------cloumn name : {column_name}----------------------------------------------")
            print("\n----------------------------------")
            print(f"| You Select {column_name} |")
            print("----------------------------------")

            # user input for , old value and new value
            print("\n.....................................................................................")
            which_delete = input(f"Which Record You Want To Update From {column_name}, Enter The value : ")
            new_value = input(f"You Want to Update {which_delete}, Enter New Value : ")
            print(".....................................................................................")

            # SQL query for updateing
            query1 = f"UPDATE {table_name} SET {column_name} = '{new_value}' WHERE {primary_field} = {primary_value}"  # Update Query
            mycursor.execute(query1)
            mydb.commit()

            # check wheather the enter value updated successfully or not.
            if mycursor.rowcount == 0:
                print(f"OPps!!!.It seems like you entered wrong value...\nWhich not in '{column_name}' column.")
                print("....................................")
                print(mycursor.rowcount, "Row Effected")
                print("....................................")
            else:
                print("....................................")
                print(mycursor.rowcount, "Record Updated Successfully")
                print("....................................")
            # end
            # exit() # have to change here

            jj = input(f"If you want to Update Again From ({table_name}) table (Press 0 for Yes) : ")
            print("\n...................................................................................")
            if jj == '0':
                continue
            else:
                break

        else:
            print("---------------------------------------------------------------------------------")
            print(f"Something went Wrong...\nYou Entered Wrong Number.....!!")
            in_again = input("Do You Want to Enter Again ?(Type 0 for Yes) : ")
            if in_again == "0":
                # print("*********************************************************************************")
                # print("*********************************************************************************")
                print("---------------------------------------------------------------------------------")
                continue
            else:
                # exit("Thanks for chossing us..")
                break


# End Update function


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
        print(
            "----------------------------------------------------------------------------------------------------------------------")
        print("1.Insert Data   2.Delete Data   3.Read Data   4.Update Data   5.Exit ", end="|")
        st = input(" What Do You Want To Do, Insert (1 to 5) : ")
        print(
            "\n---------------------------------------------------------------------------------------------------------------------")
        if st == "1":
            insert_data(mydb)
        elif st == "2":
            delete_data(mydb)
        elif st == "3":
            read_op(mydb)
        elif st == "4":
            update_op(mydb)
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
    print("Opps...Connection Not Successful!!!!\n Or Some Error Occur")
    print(e)
    print("----------------------------------------------------------------------------------")
