'''@Author : Antony Alex
   @version: Python 3.7
   @purpose: Addressbook program python'''

import json
import os
from abc import ABC, abstractmethod

class Address(ABC):
    # creating and initializing an address
    def __init__(self, address, city, state, zip_code, phone_number):
        
        self.address = address
        self.city = city
        if self.city.isdigit():
            raise ValueError
        self.state = state
        if self.state.isdigit():
            raise ValueError
        try:
            self.zip_code = int(zip_code)
        except ValueError as e:
            print(e)
        try:
            self.phone_number = int(phone_number)
        except ValueError as e:
            print(e)
        #if self.phone_number.isalpha():
            #raise ValueError

class PersonAddress(Address):
    # creating and initializing a person's address
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number):
        super().__init__(address, city, state, zip_code, phone_number)
        self.first_name = first_name
        if not self.first_name.isalpha():
            raise ValueError
        self.last_name = last_name
        if not self.last_name.isalpha():
            raise ValueError
    
    def name_print(self):
        temp_list = [self.first_name]
        temp_list.append(self.last_name)
        return ' '.join(temp_list)

    def __str__(self):
        lines = [self.name_print()]
        lines.append(self.address)
        lines.append(f'{self.city}, {self.state} {self.zip_code}')
        lines.append(str(self.phone_number))
        return '\n'.join(lines)

class Addressformat:

    def print_address(self,address):
        print_list = []
        print_list.append("{} {}".format(address.first_name, address.last_name))
        print_list.append("{}, {}".format(address.address, address.city))
        print_list.append("{} {}".format(address.state, address.zip_code))
        print_list.append("{}".format(address.phone_number))

        return print_list

class InputAddress:

    def __init__(self):
        self.new_person = None
    
    def input_address(self):
        first_name = str(input('Enter the first name : '))
        last_name = str(input('Enter the last name : '))
        address = str(input('Enter the address : '))
        city_name = str(input('Enter the city name : '))
        state = str(input('Enter the state : '))
        zipcode = int(input('Enter the zip code : '))
        phone_number = int(input('Enter the phone number : '))

        return PersonAddress(first_name, last_name, address, city_name, state, zipcode, phone_number)
         

class NameInput:
    def __init__(self):
        self.first_name = str(input("Enter the first name : "))
        self.last_name = str(input("Enter the last name :"))
    def names(self):    
        return self.first_name, self.last_name
        


class AddressBook:
    # creating and initializing an Addressbook
    def __init__(self,Bookname):
        self.Bookname = Bookname
        self.element_in_address_book = []

    def add_person(self): 
        new_input = InputAddress()
        address_new = new_input.input_address()
        print(address_new)
        self.element_in_address_book.append(address_new)
        action = int(input("Press 1 -> If you want to enter another object (Else enter any other key) :"))
        if (action == 1):
            self.add_person()
        else:
            self.addressbook_operation()

    def delete_address(self):
        print("\r")
        print("Enter the details of person that you want to delete : ")
        for address in self.element_in_address_book:
            print("\r")
            print(address)
        new_name = NameInput()
        first_name_delete, last_name_delete = new_name.names()
        flag = True
        for person in self.element_in_address_book:
            if(person.first_name == first_name_delete and person.last_name == last_name_delete):
                self.element_in_address_book.remove(person)
                print("{}, successfully deleted".format(first_name_delete))
                flag = False
        if(flag == True):
            print("No such address exists!!!")
        self.addressbook_operation()

    def addressbook_operation(self):

        print('''\n\t     1 -> Add an address
             2 -> Edit an address
             3 -> Delete an address
             4 -> Print in mailing list
             5 -> Sort by name
             6 -> Sort by ZIP
             7 -> Save the existing Addressbook
             8 -> Return to main menu''')
        try:
            operation = int(input("\nEnter operation :"))
        except ValueError as a:
            print(a)
        try:
            if(operation == 1):
                self.add_person()
            elif(operation == 2):
                self.edit_address()
            elif(operation == 3):
                self.delete_address()
            elif(operation == 4):
                self.print_in_mailing_list()
            elif(operation == 5):
                self.sort_by_name()
            elif(operation == 6):
                self.sort_by_zip()
            elif(operation == 7):
                self.save_addressbook()
            elif(operation == 8):
                return self
            else:
                print("\nWrong Selection, Try again!!")
                self.addressbook_operation()
        except UnboundLocalError as e:
            print(e)

    def edit_already_existing_addressbook(self, list_address):
        self.element_in_address_book = list_address
        self.addressbook_operation()

       

  
    def edit_address(self):
        print("\r")
        print("Enter the details of person that you want to edit : ")
        for address in self.element_in_address_book:
            print("\r")
            print(address)
        new_name = NameInput()
        first_name_edit, last_name_edit = new_name.names()
        flag = True
        for person in self.element_in_address_book:
            if(person.first_name == first_name_edit and person.last_name == last_name_edit):
                edit_address = InputAddress()
                new_address = edit_address.input_address()
                person = new_address
                flag = False   
                break
        if(flag == True):
            print("No such address exists!!!")
        self.addressbook_operation()
    
    def print_in_mailing_list(self):
        details = int(input('''\n\t     1 -> Print entire address book in mailing list format
             2 -> Print a particular address from the book\n
             '''))
        if(details == 1):
            for person in self.element_in_address_book:
                print(person)
             
            
        elif(details == 2):
            new_name = NameInput()
            first_name_print, last_name_print = new_name.names()
            flag = True
            for person in self.element_in_address_book:
                if(person.first_name == first_name_print and person.last_name == last_name_print):
                        print("\r")
                        print(person)
                        flag = False
                if(flag == True):
                    print("\nAddress does not Exist!!!")
        self.addressbook_operation()

    def sort_by_name(self):
        self.element_in_address_book.sort(key = lambda x: (x.first_name, x.last_name))
        print("\r")
        for person in self.element_in_address_book:
                print(person)
        self.addressbook_operation()
    
    def sort_by_zip(self):
        self.element_in_address_book.sort(key = lambda x: x.zip_code)
        print("\r")
        for person in self.element_in_address_book:
                print(person)
        self.addressbook_operation()
    
    def create_list_append(self):
        invent_dict = read_file()
        for inventory in invent_dict['Inventories']:
            invent_obj = Inventory(inventory['name'],inventory['weight_in_kg'],inventory['price_per_kg'])
            self.inventory_list.append(invent_obj)
    
    def save_addressbook(self):
        printer = Addressformat()
        save_list = []
        name_to_save = self.Bookname
        file_name =  "/home/admin-1/Antony_Alex/Addressbook/Saved_addressbook/" + name_to_save + '.json'
        New_address = {"Addresses" : []}            
        for address in self.element_in_address_book:
            #address_obj = PersonAddress(address['first_name'],address['last_name'],address['Address'],address['City'],address['State'],address['Zip_code'],address['Phone_number'])
            dictionary = {"first_name": address.first_name,"last_name": address.last_name,"Address": address.address,"City":address.city,"State": address.state,"Zip_code": address.zip_code,"Phone_number":address.phone_number}
            New_address["Addresses"].append(dictionary)
        file_object = open(file_name, 'w+')
        json.dump(New_address, file_object,indent=2)

class MainMenu:
    def __init__(self):
        self.addressbooks = []
    
    def Mainmenu_operation(self):
        print('''\n\t     1 -> Open a new Address book
             2 -> Delete an addressbook
             3 -> Open a saved addressbook
             4 -> Exit
             ''')
        try:
            operation = int(input("\nEnter operation :"))
        except ValueError as a:
            print(a)
        try:
            if(operation == 1):
                self.new_addressbook()
            elif(operation == 2):
                self.delete_address()
            elif(operation == 3):
                self.open_addressbook()
            elif(operation == 4):
                self.Main_menu_exit()
            else:
                print("\nWrong Selection, Try again!!")
                self.Mainmenu_operation()

        except UnboundLocalError as e:
            print(e)


    def new_addressbook(self):
        Addressbook_name = str(input("Enter a name for your new addressbook : "))
        Addressbook_name = AddressBook(Addressbook_name)
        self.addressbooks.append(Addressbook_name)
        Addressbook_name.addressbook_operation()

        self.Mainmenu_operation()
    
    def open_addressbook(self):

        print(os.listdir("/home/admin-1/Antony_Alex/Addressbook/Saved_addressbook"))
        file_to_open = str(input("Enter the file to open : "))

        try:
            with open("/home/admin-1/Antony_Alex/Addressbook/Saved_addressbook/"+file_to_open) as f:
                data = json.load(f)
            self.create_list_append(data, file_to_open)
            # file_to_read = open("e:/Addressbook/New_Addressbook/Saved_addressbook/"+file_to_open,"r")
            # file_to_read = file_to_read.read()
        except FileNotFoundError:
            print("File does not exist!!!")

        self.Mainmenu_operation()
    
    def create_list_append(self, Addresses, name):
        address_dict = Addresses
        address_list = []
        for address in address_dict['Addresses']:
            address_obj = PersonAddress(address['first_name'],address['last_name'],address['Address'],address['City'],address['State'],address['Zip_code'],address['Phone_number'])
            address_list.append(address_obj)
            print("\r")
            print(address_obj)
            print("\r")
        action = int(input("Enter 1 if you want to edit the addressbook : "))
        file_to_open = name.replace(".json","")
        file_to_open = AddressBook(file_to_open)
        if(action == 1):
            file_to_open.edit_already_existing_addressbook(address_list)
        else:
            self.Mainmenu_operation()

        
    def delete_address(self):
        print(os.listdir("/home/admin-1/Antony_Alex/Addressbook/Saved_addressbook"))
        file_to_delete = str(input("Enter the file to delete : "))
        try:
            os.remove(file_to_delete)
        except FileNotFoundError as d:
            print(d)

        self.Mainmenu_operation()
    
    @staticmethod
    def Main_menu_exit():
        exit()

def main():
    new_book = MainMenu()
    new_book.Mainmenu_operation()

if __name__ == "__main__":
    main()