from personaddress import PersonAddress
import json
    
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

class AddressBook:
    # creating and initializing an Addressbook
    def __init__(self,Bookname):
        self.Bookname = Bookname
        self.element_in_address_book = []

    def add_person(self):
        #Adds an address to the addressbook 
        address_new = input_address()
        print(address_new)
        self.element_in_address_book.append(address_new)
        try:
            action = int(input("Press 1 -> If you want to enter another object (Else enter any other digit) :"))
        except ValueError:
            print("Invalid Value!!!!")
            raise
        if (action == 1):
            self.add_person()
        elif(action>1 and action <9):
            return
        
            

    def delete_address(self):
        #Deletes an address from the addressbook
        print("\r")
        
        for address in self.element_in_address_book:
            print("\r")
            print(address)
        print("Enter the details of person that you want to delete : ")
        name_to_delete = name_input()
        flag = True
        for address in self.element_in_address_book:
            if(address.get_name() == name_to_delete):
                self.element_in_address_book.remove(address)
                print("{}, successfully deleted".format(name_to_delete))
                flag = False
                break
        if(flag == True):
            print("No such address exists!!!")
        return

    def edit_already_existing_addressbook(self, list_address):
        #Opens a new addressbook from saved files
        self.element_in_address_book = list_address
        return

    def edit_address(self):
        #Edits an address in the addressbook
        print("\r")
        print("Enter the details of person that you want to edit : ")
        for address in self.element_in_address_book:
            print("\r")
            print(address)
        address_to_find = name_input()
        flag = True
        for address in self.element_in_address_book:
            if(address.get_name() == address_to_find):
                new_address = input_address()
                address = new_address
                flag = False   
                break

        if(flag == True):
            print("No such address exists!!!")
        return
    
    def print_in_mailing_list(self):
        #Print the required address or the entire addressbook in a mailing list
        details = int(input('''\n\t     1 -> Print entire address book in mailing list format
             2 -> Print a particular address from the book\n
             '''))
        if(details == 1):
            adddressbook_print(self.element_in_address_book)
                         
        elif(details == 2):
            address_to_print = name_input()
            flag = True
            for address in self.element_in_address_book:
                if(address.get_name() == address_to_print):
                        print("\r")
                        print(address)
                        flag = False
                if(flag == True):
                    print("\nAddress does not Exist!!!")
        return 

    def sort_by_name(self):
        #Sort the addressbook by name
        self.element_in_address_book.sort(key = lambda x: (x.first_name, x.last_name))
        print("\r")
        adddressbook_print(self.element_in_address_book)
        return
    
    def sort_by_zip(self):
        #Sort the addressbook by zipcode
        self.element_in_address_book.sort(key = lambda x: x.zip_code)
        print("\r")
        adddressbook_print(self.element_in_address_book)
        return
     
    def save_addressbook(self):
        #Save the addressbook to a json file
        name_to_save = self.Bookname
        file_name =  "/home/admin-1/Antony_Alex/Addressbook/Saved_addressbook/" + name_to_save + '.json'
        New_address = {"Addresses" : []}            
        for address in self.element_in_address_book:
            dictionary = {"first_name": address.first_name,"last_name": address.last_name,"Address": address.address,"City":address.city,"State": address.state,"Zip_code": address.zip_code,"Phone_number":address.phone_number}
            New_address["Addresses"].append(dictionary)
        file_object = open(file_name, 'w+')
        json.dump(New_address, file_object,indent=2)
        return

    def __len__(self):
        return len(self.element_in_address_book)

def adddressbook_print(list_of_addresses):
    for address in list_of_addresses:
        print(address)
        print("\n")
    