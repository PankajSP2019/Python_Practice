# Mini project #1
# Online Library System
from datetime import datetime


class bcolour:
    green = '\033[92m'  # green
    yellow = '\033[93m'  # yellow
    red = '\033[91m'  # red
    blue = '\033[94m'  # blue
    h1 = '\033[100m'  # white colour with highlight
    h2 = '\033[101m'  # white colour with red highlight
    h3 = '\033[102m'  # white colour with green highlight
    reset = '\033[0m'  # reset


class Library:
    list_of_books = list()
    library_name = str()
    lend_dict = dict()

    def __init__(self, nm):
        # Available Book
        # if we use read/readlines there will be an extra \n with the string ,to remove this we use read().splitlines()
        file = open("Books.txt", "r")
        items = file.read().splitlines()
        file.close()
        # print(items)

        self.list_of_books = items
        self.library_name = nm
        # print(self.list_of_books)

        # Lend book
        file1 = open("Book_lend.txt", "r")
        items1 = file1.read().splitlines()
        # print(f"Length of LEND : {len(items1)}")

        # if len(items1) > 2:
        #     for i in range(0, len(items1)):
        #         name1 = items1[i].split(":")[0]
        #         book = items1[i].split(":")[1]
        #         self.lend_dict[name1] = book
        # else:
        #     print("No Book Is On Lend")
        try:
            for i in range(0, len(items1)):
                name1 = items1[i].split(":")[0]
                book = items1[i].split(":")[1]
                self.lend_dict[name1] = book
        except Exception as e:
            print(e)
            print("No Book is On Lend")

        file1.close()

    def DisplayUser(self):
        print(bcolour.blue + "-------------------All Available Books-------------------" + bcolour.reset)
        file = open("Books.txt", "r")
        items = file.readlines()
        for i in range(1, len(items)):
            print(items[i], end="")
        # print("\n===========================")
        # print(bcolour.red + f"In Rent Book List : {self.lend_dict}" + bcolour.reset)
        # print("===========================")
        # print(bcolour.green + f"Total Book In Library : {len(self.list_of_books) - 1}" + bcolour.reset)
        # print(bcolour.red + f"Total Book In Lend : {len(self.lend_dict)}" + bcolour.reset)
        print(bcolour.blue + "---------------------------------------------------------" + bcolour.reset)
        file.close()

    def DisplayBooks(self):
        print(bcolour.blue + "-------------------All Available Books-------------------" + bcolour.reset)
        file = open("Books.txt", "r")
        items = file.readlines()
        for i in range(1, len(items)):
            print(items[i], end="")
        print(bcolour.red + "\n======================Lend List==========================")
        print(f"In Lend Book List : {self.lend_dict}")
        print(bcolour.green + "\t\tBook : Name" + bcolour.reset)
        print("\t\t...........")
        for i in self.lend_dict:
            print(bcolour.blue + f"\t\t{i} : {self.lend_dict.get(i)}\t\t" + bcolour.reset)
        print(bcolour.red + "=========================================================" + bcolour.reset)
        print(bcolour.green + f"Total Book In Library : {len(self.list_of_books) - 1}" + bcolour.reset)
        print(bcolour.red + f"Total Book In Lend : {len(self.lend_dict)}" + bcolour.reset)
        print(bcolour.blue + "---------------------------------------------------------" + bcolour.reset)
        file.close()

    def lendBook(self, nm):

        while True:
            bn = input("Enter The Book Name (Type n For Exit : ) : ")
            f = open("Books.txt", "r")
            ooo = f.read().splitlines()
            # print(ooo)
            f.close()
            if bn == 'n':
                break
            if bn in ooo:
                self.lend_dict[bn] = nm
                self.list_of_books.remove(bn)
                # Delete From text File
                with open("Books.txt", "r") as f:
                    data = f.readlines()
                with open("Books.txt", "w") as f:
                    for line in data:
                        if line.strip("\n") != bn:
                            f.write(line)
                # Add in book lend file (.txt)
                file2 = open("Book_lend.txt", 'a')
                file2.write(bn + ":" + nm + "\n")
                print(bcolour.red + "........................................" + bcolour.reset)
                print(f"Book Name : '{bn}' Landed By : '{nm}'\t\t\t\t\t Time : {datetime.now()} ")
                with open("Library_log.txt","a") as f:
                    f.write(f"Book Name : '{bn}' Landed By : '{nm}'\t\t\t\t\t Time : {datetime.now()}\n")
                print(bcolour.red + "........................................" + bcolour.reset)
                break
            else:
                print(f"'{bn}' is not the Right name\nTry Again")
                continue

    def addBook(self, book_nm):
        self.list_of_books.append(book_nm)
        file = open("Books.txt", "a")
        file.write(book_nm + "\n")
        print(bcolour.yellow + "........................................" + bcolour.reset)
        print(f"'{book_nm}' Book Add To The Library")
        print("Thanks For Donate The Book")
        with open("Library_log.txt","a") as f:
            f.write(f"'{book_nm}' Book Add To The Library\t\t\t\t\t Time : {datetime.now()}\n")
        print(bcolour.yellow + "........................................" + bcolour.reset)

    def ReturnBook(self, book_nm):
        while True:
            name = input("Enter Your Name (Type n if Exit) : ")

            ty = book_nm + ":" + name
            fi = open("Book_lend.txt", "r")
            ty1 = fi.read().splitlines()
            fi.close()

            if name == 'n':
                break

            if book_nm in self.lend_dict and ty in ty1:
                self.lend_dict.pop(book_nm)
                self.list_of_books.append(book_nm)
                # Add returned book in the library
                with open("Books.txt", "a") as f:
                    f.write(book_nm + "\n")
                # Delete From text File
                with open("Book_lend.txt", "r") as f:
                    data = f.readlines()
                with open("Book_lend.txt", "w") as f:
                    for line in data:
                        if line.strip("\n") != ty:
                            f.write(line)
                print(bcolour.green + "........................................" + bcolour.reset)
                print(f"Successfully Return the Book : '{book_nm}' ")
                with open("Library_log.txt", "a") as f:
                    f.write(f"Successfully Return the Book : '{book_nm}' \t\t\t\t\t Time : {datetime.now()}\n")
                print(bcolour.green + "........................................" + bcolour.reset)
            else:
                print(bcolour.red + "........................................" + bcolour.reset)
                print(f"{book_nm} is not the Right Book name Or Check Your Name")
                print(bcolour.red + "........................................" + bcolour.reset)
            break


if __name__ == '__main__':
    l1 = Library("Pankaj's Library")

    print(bcolour.yellow + f"\t\t\t\t\t\t\t\t{l1.library_name}" + bcolour.reset)
    while True:
        try:
            x = int(
                input(bcolour.green + "1.(Show All Available Books)  2.(Lend Book)  3.(Donate Book)  4.(Return Book)  "
                                      "5.(Admin)  6.(Exit)\nSelect : " + bcolour.reset))
        except Exception as e:
            print(bcolour.h2 + "------------------------------------------" + bcolour.reset)
            print(e)
            print("Wrong Input Try Again")
            print(bcolour.h2 + "------------------------------------------" + bcolour.reset)
            continue

        if x == 1:
            l1.DisplayUser()
        elif x == 2:
            lender_name = input("Enter Your Name : ")
            l1.lendBook(lender_name)
        elif x == 3:
            book_name = input("Enter Book Name : ")
            l1.addBook(book_name)
        elif x == 4:
            book_name = input("Enter Book Name : ")
            l1.ReturnBook(book_name)
        elif x == 5:
            print(bcolour.red + "----------------------Admin Panel--------------------" + bcolour.reset)
            username = input("Enter User Name : ")
            password = input("Enter PassWord : ")

            if username == "admin123" and password == "admin123":
                while True:
                    try:
                        n = int(input(bcolour.yellow + "1.(All Available Books And on Lend) 2.(Book File) 3.(Lend "
                                                       "File) 4.(Log "
                                                       "Book) 5.(back Main Menu) 6.(Exit)\nSelect : " + bcolour.reset))
                        if n == 1:
                            l1.DisplayBooks()

                        elif n == 2:
                            with open("Books.txt", "r") as f:
                                it = f.read().splitlines()
                                for i in it:
                                    print(i)
                        elif n == 3:
                            with open("Book_lend.txt", "r") as f:
                                it1 = f.read().splitlines()
                                for i in it1:
                                    print(i)
                        elif n == 4:
                            print("---------------Library Log Book---------------")
                            with open("Library_log.txt","r") as f:
                                tt = f.read().splitlines()
                                for i in tt:
                                    print(bcolour.blue + f"\t{i}" + bcolour.reset)
                        elif n == 5:
                            print(bcolour.red + "----------------------Admin Panel Exit--------------------" + bcolour.reset)
                            break
                        elif n == 6:
                            print(
                                bcolour.red + "----------------------Admin Panel Exit--------------------" + bcolour.reset)
                            exit('Thanks For Choosing Us\nHave a Nice Day')
                    except Exception as e:
                        print("Wrong Input ..Try again")
                        continue
            else:
                print("Wrong User Name / Password")
                print("Try Again")
                continue

            print(bcolour.red + "------------------------------------------" + bcolour.reset)
        elif x == 6:
            print(bcolour.red + "------------------------------------------" + bcolour.reset)
            exit('Thanks For Choosing Us\nHave a Nice Day')
        else:
            print("Wrong Input\nTry Again")
