"""
Author : Pankaj Kumar Das
Date : 23/02/2023
Purpose : Develop a Computer  Lab Management Application Using Python
Problem Name : Lab Manager
"""

import json
from prettytable import PrettyTable  # for , show all the details in a pretty table format


# loads() takes in a string and returns a json object. json. dumps() takes in a json object and returns a string.


# just color the text in console
class bcolour:
    green = '\033[92m'  # green
    yellow = '\033[93m'  # yellow
    red = '\033[91m'  # red
    blue = '\033[94m'  # blue
    h1 = '\033[100m'  # white colour with highlight
    h2 = '\033[101m'  # white colour with red highlight
    h3 = '\033[102m'  # white colour with green highlight
    reset = '\033[0m'  # reset


class Lab:
    all_data = list()
    pc_numbers = list()

    def __init__(self):
        with open("data.txt", 'r') as f:
            data = f.readlines()

        # all data from text file, in json format (string to json), store in a variable with json.loads function
        self.all_data = [json.loads(i.strip()) for i in data if i != "\n"]

    def add_pc(self, x):
        """
        :param x: How many pc want to add
        :return: nothing will be return , just add the pc
        """
        try:
            adding_data = list()
            for i in range(x):
                temp_dict = dict()
                print(f"-------------------------{i + 1}----------------------------")
                pc_numbers = [i.get("pc_number") for i in self.all_data]
                pc_no = int(input("Enter PC number : "))
                if pc_no not in pc_numbers:

                    os_name = input("Enter OS Name : ")
                    # add in dictonary
                    temp_dict["pc_number"] = pc_no
                    temp_dict["operating_system"] = os_name

                    h = int(input("Any Problem in PC, Enter number how may problem identify (else enter 0): "))
                    if h == 0:
                        status = "ok"
                        temp_dict["status"] = status
                    else:
                        status_list = list()
                        for i in range(h):
                            print(f"--------------------{i + 1}--------------------")
                            p = input("Enter Problem : ")
                            status_list.append(p)
                        temp_dict["status"] = status_list

                    # add the new data in the main data list
                    self.all_data.append(temp_dict)
                    # add the new data in the .txt file
                    with open("data.txt", 'a') as f:
                        f.write("\n" + json.dumps(temp_dict))
                    print("---------------------------------------------")
                    print(bcolour.green + f"PC_ON : {pc_no} Added to the Lab Successfully" + bcolour.reset)
                    print("---------------------------------------------")
                else:
                    print(bcolour.red + "--------------------------------------------")
                    print(f"This PC Number : {pc_no} is Already Exists" + bcolour.reset)
                    x = input(f"For this PC : {pc_no} ,Select : 1.Modify Information 2.Remove OR Enter anything to "
                              f"Exit  : ")

                    if x == '1':
                        # modify information
                        self.update_pc(pc_no)
                        pass
                    elif x == '2':
                        # Remove pc from lab
                        self.remove_pc(pc_no)
                        pass
                    else:
                        continue

        except Exception as e:
            print(e)

    def remove_pc(self, x):
        """
        This method is for remove the pc from the lab
        :param x: PC number want to delete
        :return: nothing will be return just remove the pc from lab
        """
        pc_numbers = [i.get("pc_number") for i in self.all_data]

        try:
            if self.search_pc(sorted(pc_numbers), x):
                # index number of the pc
                index = pc_numbers.index(x)
                # information we want to remove, store in a variable
                ty = json.dumps(self.all_data[index])
                # pop the pc from the list
                self.all_data.pop(index)
                # remove the pc from the text file
                with open("data.txt", "r") as f:
                    data = f.readlines()
                with open("data.txt", "w") as f:
                    for line in data:
                        if line.strip("\n") != ty:
                            f.write(line)
                print("---------------------------------------------")
                print(bcolour.red + f"PC_ON : {x} Remove From the Lab Successfully" + bcolour.reset)
                print("---------------------------------------------")
            else:
                print("--------------------------------------")
                print(bcolour.red + "This Pc NOT Found in LAB" + bcolour.reset)
                print("--------------------------------------")
        except Exception as e:
            print(bcolour.red + "-------------------------------------------------------")
            print(e)
            print("Something Went Wrong Please try again")
            print("-------------------------------------------------------" + bcolour.reset)

    def update_pc(self, x):
        """
        This method will use for the information of pc
        :param x: Pc number want to update information
        :return: Nothing will be return just update the the pc's information
        """
        # all the pc number in a list
        pc_numbers = [i.get("pc_number") for i in self.all_data]

        try:
            if self.search_pc(sorted(pc_numbers), x):
                # index number of the pc
                index = pc_numbers.index(x)

                print(bcolour.red + "You Can not Update/Modify the PC Number" + bcolour.reset)
                n = input(bcolour.blue + "Want Update IN : 1.Operating System 2.Status (type anything to exit this "
                                         "option)\nSelect : " + bcolour.reset)
                if n == '1':
                    print(f"Current Operating System of this PC : {self.all_data[index].get('operating_system')}")
                    up_os = input("Please Enter The Updated OS : ")
                    self.all_data[index]['operating_system'] = up_os
                    with open("data.txt", "w") as f:
                        for line in self.all_data:
                            f.write("\n" + json.dumps(line))
                    print("---------------------------------------------")
                    print(bcolour.green + f"PC_ON : {x} Updated Successfully" + bcolour.reset)
                    print("---------------------------------------------")
                elif n == '2':
                    print(f"Current Status of this PC : {self.all_data[index].get('status')}")
                    if self.all_data[index].get('status') == "ok":
                        d = input("Any Problem Found ?(enter y for yes): ")
                        if d == 'y':
                            h = int(input("Any Problem in PC, Enter number how may problem identify (else enter 0): "))
                            if h != 0:
                                status_list = list()
                                for i in range(h):
                                    print(f"--------------------{i + 1}--------------------")
                                    p = input("Enter Problem : ")
                                    status_list.append(p)
                                # add the Updated data in the main list
                                self.all_data[index]['status'] = status_list
                                # add the add in the data file
                                with open("data.txt", "w") as f:
                                    for line in self.all_data:
                                        f.write("\n" + json.dumps(line))
                                print("---------------------------------------------")
                                print(bcolour.green + f"PC_ON : {x} Updated Successfully" + bcolour.reset)
                                print("---------------------------------------------")
                            else:
                                print("---------------------------------------------")
                                print(bcolour.green + f"PC_ON : {x} NO Updated Done" + bcolour.reset)
                                print("---------------------------------------------")
                        else:
                            print("---------------------------------------------")
                            print(bcolour.green + f"PC_ON : {x} NO Updated Done" + bcolour.reset)
                            print("---------------------------------------------")
                    else:
                        d1 = input("1.All the Problem Solved 2.Add More Problem \nSelect : ")
                        if d1 == '1':
                            # add the Updated data in the main list
                            self.all_data[index]['status'] = "ok"
                            # add the add in the data file
                            with open("data.txt", "w") as f:
                                for line in self.all_data:
                                    f.write("\n" + json.dumps(line))
                            print("---------------------------------------------")
                            print(bcolour.green + f"PC_ON : {x} Updated Successfully" + bcolour.reset)
                            print("---------------------------------------------")
                        elif d1 == '2':
                            self.all_data[index]['status'].append("mouse problem")

                            h = int(input("Any Problem in PC, Enter number how may problem identify (else enter 0): "))
                            if h != 0:
                                for i in range(h):
                                    print(f"--------------------{i + 1}--------------------")
                                    p = input("Enter Problem : ")
                                    self.all_data[index]['status'].append(p)
                                # add the add in the data file
                                with open("data.txt", "w") as f:
                                    for line in self.all_data:
                                        f.write("\n" + json.dumps(line))
                                print("---------------------------------------------")
                                print(bcolour.green + f"PC_ON : {x} Updated Successfully" + bcolour.reset)
                                print("---------------------------------------------")
                            else:
                                print("---------------------------------------------")
                                print(bcolour.green + f"PC_ON : {x} NO Updated Done" + bcolour.reset)
                                print("---------------------------------------------")
                else:
                    print("---------------------------------------------")
                    print(bcolour.green + f"PC_ON : {x} NO Updated Done" + bcolour.reset)
                    print("---------------------------------------------")
            else:
                print("--------------------------------------")
                print(bcolour.red + "This Pc NOT Found in LAB" + bcolour.reset)
                print("--------------------------------------")
        except Exception as e:
            print(bcolour.red + "-------------------------------------------------------")
            print(e)
            print("Something Went Wrong Please try again")
            print("-------------------------------------------------------" + bcolour.reset)

    def display_all_pc(self):
        t = PrettyTable(["PC_NUMBER", "OPERATING SYSTEM", "STATUS"])
        for i in self.all_data:
            tmp_list = list()
            tmp_list.append(i['pc_number'])
            tmp_list.append(i['operating_system'])
            tmp_list.append(i['status'])
            t.add_row(tmp_list)
        print(bcolour.green)
        print(t)
        print(bcolour.reset)

    def display_individual_pc(self, x):
        """
        This method takes pc number as parameter, and check weather the pc number is in the lab or not,
        if the pc is exist in the lab then , prompt up a message that user to show the details or not.
        And if the pc not in lab then , then prompt a message for add new pc in the lab
        :param x: PC Number Want to Search
        :return: Display thr individual pc information
        """
        pc_numbers = [i.get("pc_number") for i in self.all_data]
        if self.search_pc(sorted(pc_numbers), x):
            print(bcolour.green + "This Pc Found in LAB" + bcolour.reset)
            print("--------------------------------------")
            d = input("Do You Want To Show The Details Of this PC? (press 1 to yes) : ")
            if d == '1':
                # find the index number
                index = pc_numbers.index(x)
                print(bcolour.blue + "--------------------------------------")
                for i, j in self.all_data[index].items():
                    print(f"{i} : {j}")
                print("--------------------------------------" + bcolour.reset)
            else:
                print(bcolour.red + "--------------------------------------")
                print("Successfully Exit This Option")
                print("--------------------------------------" + bcolour.reset)
        else:
            print("--------------------------------------")
            print(bcolour.red + "This Pc NOT Found in LAB" + bcolour.reset)
            print("--------------------------------------")
            x = input("Do You Want To Add New PC In The Lab? (press 1 to yes) : ")
            if x == '1':
                # adding the pc
                self.add_pc(1)
            else:
                print(bcolour.red + "--------------------------------------")
                print("Successfully Exit This Option")
                print("--------------------------------------" + bcolour.reset)

    def search_pc(self, list1, x):
        """
        This method will perform binary search
        :param list1: A sorted list takes as a input
        :param x: which element want to search in the list
        :return: is the element , is in the list or not (ture/ false)
        """
        # lower bound
        l = 0
        # Upper bound
        u = len(list1) - 1
        while l <= u:
            # mid position
            m = (l + u) // 2
            if list1[m] == x:
                return True
            else:
                if list1[m] < x:
                    l = m + 1
                else:
                    u = m - 1
        return False


if __name__ == "__main__":
    l1 = Lab()
    while True:
        try:
            print(bcolour.blue + "----------------------------------------------------------------------")
            hh = input("1.Add PC 2.Update PC 3.Remove PC 4.Search PC 5.Display All PC 6.Exit \nSelect: ")
            print(bcolour.blue + "----------------------------------------------------------------------"
                  + bcolour.reset)

            if hh == '1':
                while True:
                    x = int(input("How Many Pc You Want to add : "))
                    l1.add_pc(x)
                    d = input("Do You Want to ADD More ?(press y for Yes): ")
                    if d == 'y':
                        continue
                    else:
                        break
            elif hh == '2':
                while True:
                    x = int(input("Enter The PC NUMBER : "))
                    l1.update_pc(x)
                    d = input("Do You Want to Update More ?(press y for Yes): ")
                    if d == 'y':
                        continue
                    else:
                        break
            elif hh == '3':
                while True:
                    x = int(input("Enter The PC NUMBER : "))
                    l1.remove_pc(x)
                    d = input("Do You Want to Remove More ?(press y for Yes): ")
                    if d == 'y':
                        continue
                    else:
                        break
            elif hh == '4':
                while True:
                    x = int(input("Enter The PC NUMBER : "))
                    l1.display_individual_pc(x)
                    d = input("Do You Want to Search More ?(press y for Yes): ")
                    if d == 'y':
                        continue
                    else:
                        break
            elif hh == '5':
                while True:
                    l1.display_all_pc()
                    d = input("Do You Want to Display Again ?(press y for Yes): ")
                    if d == 'y':
                        continue
                    else:
                        break
            elif hh == '6':
                exit("Thanks For Being With US\nSuccessfully "
                     "Exit\n----------------------------------------------------------------------"+bcolour.reset)

            else:
                print("It Seems like like, you Entered Wrong Number \nPlease try again.")
            # main condition
        # main loop
        except Exception as e:
            print(bcolour.red + "-------------------------------------------------------")
            print(e)
            print("Something Went Wrong Please try again")
            print("-------------------------------------------------------" + bcolour.reset)

