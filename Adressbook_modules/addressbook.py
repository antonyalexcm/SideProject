from personaddress import PersonAddress
import json

   
class AddressBook:
    '''Class : Addressbook'''
    # creating and initializing an Addressbook
    def __init__(self,Bookname):
        self.Bookname = Bookname
        self.element_in_address_book = []

    def add_address(self,address_to_add):
        self.element_in_address_book.append(address_to_add)
        return
        
    def edit_already_existing_addressbook(self, list_address):
        #Opens a new addressbook from saved files
        self.element_in_address_book = list_address
        return
 
    def sort_by_name(self):
        #Sort the addressbook by name
        self.element_in_address_book.sort(key = lambda x: (x.first_name, x.last_name))
        return
    
    def sort_by_zip(self):
        #Sort the addressbook by zipcode
        self.element_in_address_book.sort(key = lambda x: x.zip_code)
        return
   
    def delete_address(self,address_to_delete):
        #Deletes an address from the addressbook
        self.element_in_address_book.remove(address_to_delete)
        return
                    
    def __len__(self):
        return len(self.element_in_address_book)