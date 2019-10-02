'''@Author : Antony Alex
   @version: Python 3.7
   @purpose: Addressbook program python'''


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


class AddressPrinter:
    def print_address(self,Address):
        print(Address)
        return

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
        self.element_in_address_book.append(address_new)
        self.addressbook_operation()

    def delete_address(self):
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
  
    def edit_address(self):
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
        printer = AddressPrinter()
        details = int(input('''\n\t     1 -> Print entire address book in mailing list format
             2 -> Print a particular address from the book\n
             '''))
        if(details == 1):
            for person in self.element_in_address_book:
                printer.print_address(person)
             
            
        elif(details == 2):
            new_name = NameInput()
            first_name_print, last_name_print = new_name.names()
            flag = True
            for person in self.element_in_address_book:
                if(person.first_name == first_name_print and person.last_name == last_name_print):
                        print("\r")
                        printer.print_address(person)
                        flag = False
                if(flag == True):
                    print("\nAddress does not Exist!!!")
        self.addressbook_operation()

    def sort_by_name(self):
        printer = AddressPrinter()
        self.element_in_address_book.sort(key = lambda x: (x.first_name, x.last_name))
        print("\r")
        for person in self.element_in_address_book:
                printer.print_address(person)
        self.addressbook_operation()
    
    def sort_by_zip(self):
        printer = AddressPrinter()
        self.element_in_address_book.sort(key = lambda x: x.zip_code)
        print("\r")
        for person in self.element_in_address_book:
                printer.print_address(person)
        self.addressbook_operation()
    
    def save_addressbook(self):
        printer = Addressformat()
        save_list = []
        name_to_save = self.Bookname
        file_name =  name_to_save + '.txt'
        for person in self.element_in_address_book:
            address_new = printer.print_address(person)
            save_list.append(address_new)
        file_new = open(file_name,"w+")
        for i in range(0, len(save_list)):
            content_to_save ='\n'.join(save_list[i]) 
            print(content_to_save)
            file_new.write(content_to_save)
        file_new.close()
        self.addressbook_operation()


class MainMenu:
    def __init__(self):
        self.addressbooks = []
    
    def Mainmenu_operation(self):
        print('''\n\t     1 -> Open a new Address book
             2 -> Delete an addressbook
             3 -> Open an addressbook
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
        Addressbook_name = str(input("Enter a name for your new addressbook name : "))
        Addressbook_name = AddressBook(Addressbook_name)
        self.addressbooks.append(Addressbook_name)
        Addressbook_name.addressbook_operation()

        self.Mainmenu_operation()

    
    def open_addressbook(self):

        print(os.listdir("e:/Addressbook/New_Addressbook/Saved_addressbook"))
        file_to_open = str(input("Enter the file to open : "))
        try:
            file_to_read = open("e:/Addressbook/New_Addressbook/Saved_addressbook/"+file_to_open,"r")
            file_to_read = file_to_read.read()

        except FileNotFoundError:
            print("File does not exist!!!")
        print(file_to_read)

        self.Mainmenu_operation()
    
    def delete_address(self):
        print(os.listdir("/Saved_addressbook"))
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