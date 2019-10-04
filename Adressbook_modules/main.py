'''@Author : Antony Alex
   @version: Python 3.7
   @purpose: Addressbook program python'''

import json
import os
from personaddress import PersonAddress
from addressbook import AddressBook

addressbooks = []
adressbook_names = []
    
def new_addressbook():
    Addressbook_name = str(input("Enter a name for your new addressbook : "))
    Addressbook_name = AddressBook(Addressbook_name)
    addressbook_operation(Addressbook_name)
    
def open_addressbook():

    print(os.listdir("/home/admin-1/Antony_Alex/Addressbook/Saved_addressbook"))
    file_to_open = str(input("\nEnter the file to open : "))
    try:
        with open("/home/admin-1/Antony_Alex/Addressbook/Saved_addressbook/"+file_to_open) as f:
            data = json.load(f)
        create_list_append(data, file_to_open)
    except FileNotFoundError:
        print("File does not exist!!!")
    mainmenu_operation()

def create_list_append(Addresses, name):
    address_dict = Addresses
    address_list = []
    for address in address_dict['Addresses']:
        address_obj = PersonAddress(address['first_name'],address['last_name'],address['Address'],address['City'],address['State'],address['Zip_code'],address['Phone_number'])
        address_list.append(address_obj)
        print("\r")
        print(address_obj)
        print("\r")
    file_to_open = name.replace(".json","")
    file_to_open = AddressBook(file_to_open)
    action = int(input("Enter 1 if you want to edit the addressbook : "))
    if(action == 1):
        file_to_open.edit_already_existing_addressbook(address_list)
        addressbook_operation(file_to_open)
    else:
        mainmenu_operation()

        
def delete_address():
    print(os.listdir("/home/admin-1/Antony_Alex/Addressbook/Saved_addressbook"))
    file_to_delete = str(input("\nEnter the file to delete : "))
    try:
        os.remove(file_to_delete)
    except FileNotFoundError as d:
        print(d)

    mainmenu_operation()

def check(addressbook_name):
    if (len(addressbook_name) > 0):
        return True
    else:
        return False
def print_no_address():
    print("Addressbook has no elements!!!")
    print("\n")
    return


def addressbook_operation(addressbook_name):

    print("The name of adressbook is : ", addressbook_name.Bookname)
    while True:
        print('''\n1 -> Add an address\n2 -> Edit an address\n3 -> Delete an address\n4 -> Print in mailing list\n5 -> Sort by name\n6 -> Sort by ZIP\n7 -> Save the existing Addressbook\n8 -> Return to main menu''')
        try:
            operation = int(input("\nEnter operation :"))
        except ValueError as a:
            print(a)
        try:
            flag = True
            if(operation == 1):
                addressbook_name.add_person()
            elif(operation == 2):
                if check(addressbook_name):
                    addressbook_name.edit_address()
                    flag = False
            elif(operation == 3):
                if check(addressbook_name):
                    addressbook_name.delete_address()
                    flag = False
            elif(operation == 4):
                if check(addressbook_name):
                    addressbook_name.print_in_mailing_list()
                    flag = False
            elif(operation == 5):
                if check(addressbook_name):
                    addressbook_name.sort_by_name()
                    flag = False
            elif(operation == 6):
                if check(addressbook_name):
                    addressbook_name.sort_by_zip()
                    flag = False
            elif(operation == 7):
                if check(addressbook_name):
                    addressbook_name.save_addressbook()
                    flag = False
            elif(operation == 8):
                mainmenu_operation()
            else:
                print("\nWrong Selection, Try again!!")
                addressbook_operation(addressbook_name)
            if(flag == True):
                print_no_address()
            addressbook_operation(addressbook_name)
        except UnboundLocalError as e:
            print(e)


def mainmenu_operation():

    while True:
        print('''\n1 -> Open a new Address book\n2 -> Delete an addressbook\n3 -> Open a saved addressbook\n4 -> Exit''')
        try:
            operation = int(input("\nEnter operation :"))
        except ValueError as a:
            print(a)
        try:
            if(operation > 0 and operation < 5):
                functions = [new_addressbook,delete_address,open_addressbook,main_menu_exit]
                functions[operation-1]()

            else:
                print("\nWrong Selection, Try again!!")
                mainmenu_operation()

        except UnboundLocalError as e:
            print(e)

def main_menu_exit():
        exit()

def main():
    mainmenu_operation()


if __name__ == "__main__":
    main()