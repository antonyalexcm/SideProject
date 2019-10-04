from abc import ABC

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