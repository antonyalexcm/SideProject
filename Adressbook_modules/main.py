'''@Author : Antony Alex
   @version: Python 3.7
   @purpose: Addressbook program python'''

import json
import os
from personaddress import PersonAddress
from addressbook import AddressBook


addressbooks = []
adressbook_names = []
    

def check(addressbook_name):
    if (len(addressbook_name) > 0):
        return True
    else:
        return False

def print_no_address():
    print("Addressbook has no elements!!!")
    print("\n")
    return

def input_address():
    first_name = str(input('Enter the first name : '))
    last_name = str(input('Enter the last name : '))
    address = str(input('Enter the address : '))
    city_name = str(input('Enter the city name : '))
    state = str(input('Enter the state : '))
    zipcode = int(input('Enter the zip code : '))
    phone_number = int(input('Enter the phone number : '))
    return PersonAddress(first_name, last_name, address, city_name, state, zipcode, phone_number)
         

def name_input():

        first_name = str(input("Enter the first name : "))
        last_name = str(input("Enter the last name :"))
        return first_name +' '+last_name

def adddressbook_print(list_of_addresses):
    for address in list_of_addresses:
        print(address)
        print("\n")


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
                add_address(addressbook_name)
            elif(operation == 2):
                if check(addressbook_name):
                    edit_addressbook(addressbook_name)
                    flag = False
            elif(operation == 3):
                if check(addressbook_name):
                    delete_address(addressbook_name)
                    flag = False
            elif(operation == 4):
                if check(addressbook_name):
                    print_in_mailing_list(addressbook_name)
                    flag = False
            elif(operation == 5):
                if check(addressbook_name):
                    addressbook_name.sort_by_name()
                    adddressbook_print(addressbook_name.element_in_address_book)
                    flag = False
            elif(operation == 6):
                if check(addressbook_name):
                    addressbook_name.sort_by_zip()
                    adddressbook_print(addressbook_name.element_in_address_book)
                    flag = False
            elif(operation == 7):
                if check(addressbook_name):
                    save_addressbook(addressbook_name)
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


def add_address(addressbook_name):
    address_new = input_address()
    print(address_new)
    addressbook_name.add_address(address_new)
    while True:
            try:
                action = int(input("Press 1 -> If you want to enter another object (Else enter any other digit) :"))
                break
            except ValueError:
                print("Invalid Value!!!!")
    if (action == 1):
        add_address(addressbook_name)
    elif(action>1 and action <9):
        return

def edit_addressbook(addressbook_name):
    print("\r")
    print("Enter the details of person that you want to edit : ")
    for address in addressbook_name.element_in_address_book:
        print("\r")
        print(address)
    address_to_find = name_input()
    flag = True
    for address in addressbook_name.element_in_address_book:
        if(address.get_name() == address_to_find):
            print(address)
            new_address = input_address()
            addressbook_name.element_in_address_book.delete_address(address)
            addressbook_name.element_in_address_book.add_address(new_address)            
            flag = False   
            break
    if(flag == True):
        print("No such address exists!!!")
    return  

def delete_address(addressbook_name):
        #Deletes an address from the addressbook
        
        for address in addressbook_name.element_in_address_book:
            print("\r")
            print(address)
        print("Enter the details of person that you want to delete : ")
        name_to_delete = name_input()
        flag = True
        for address in addressbook_name.element_in_address_book:
            if(address.get_name() == name_to_delete):
                addressbook_name.delete_address(address)
                print("{}, successfully deleted".format(name_to_delete))
                flag = False
                break
        if(flag == True):
            print("No such address exists!!!")
        return
    
def print_in_mailing_list(addressbook_name):
    #Print the required address or the entire addressbook in a mailing list
    while True:
        try:
            details = int(input('''\n\t     1 -> Print entire address book in mailing list format
                 2 -> Print a particular address from the book\n
                 '''))
            break
        except ValueError:
            print("Invalid Input!!!")
    if(details == 1):
        adddressbook_print(addressbook_name.element_in_address_book)
                     
    elif(details == 2):
        address_to_print = name_input()
        flag = True
        for address in addressbook_name.element_in_address_book:
            if(address.get_name() == address_to_print):
                    print("\r")
                    print(address)
                    flag = False
            if(flag == True):
                print("\nAddress does not Exist!!!")
    return

def  save_addressbook(addressbook_name):
    name_to_save = addressbook_name.Bookname
    file_name =  name_to_save + '.json'
    New_address = {"Addresses" : []}            
    for address in addressbook_name.element_in_address_book:
        dictionary = {"first_name": address.first_name,"last_name": address.last_name,"Address": address.address,"City":address.city,"State": address.state,"Zip_code": address.zip_code,"Phone_number":address.phone_number}
        New_address["Addresses"].append(dictionary)
    file_object = open(file_name, 'w+')
    json.dump(New_address, file_object,indent=2)
    return

def mainmenu_operation():

    print('''\n1 -> Open a new Address book\n2 -> Delete an addressbook\n3 -> Open a saved addressbook\n4 -> Exit''')
    flag = True
    while flag:
        try:
            operation = int(input("\nEnter operation :"))
            flag = False
        except ValueError as a:
            print(a)
       
    try:
        if(operation > 0 and operation < 5):
            functions = [new_addressbook,delete_addressbook,open_addressbook,main_menu_exit]
            functions[operation-1]()
        else:
            print("\nWrong Selection, Try again!!")
            mainmenu_operation()
    except UnboundLocalError as e:
        print(e)

def new_addressbook():
    Addressbook_name = str(input("Enter a name for your new addressbook : "))
    Addressbook_name = AddressBook(Addressbook_name)
    addressbook_operation(Addressbook_name)

def delete_addressbook():
    print(os.listdir())
    file_to_delete = str(input("\nEnter the file to delete : "))
    try:
        os.remove(file_to_delete)
    except FileNotFoundError as d:
        print(d)
    
    mainmenu_operation()

def open_addressbook():

    print(os.listdir())
    file_to_open = str(input("\nEnter the file to open : "))
    try:
        with open(file_to_open) as f:
            data = json.load(f)
        create_list_append(data, file_to_open)
    except FileNotFoundError:
        print("File does not exist!!!")
    except json.decoder.JSONDecodeError as err:
        print(err)
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
    while True:
        try:
            action = int(input("Enter 1 if you want to edit the addressbook(Enter any other digit to exit) : "))
        except ValueError as err:
            print(err)
        break
    if(action == 1):
        file_to_open.edit_already_existing_addressbook(address_list)
        addressbook_operation(file_to_open)
    else:
        mainmenu_operation()

def main_menu_exit():
        exit()

def main():
    mainmenu_operation()


if __name__ == "__main__":
    main()