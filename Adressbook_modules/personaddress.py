from Abstract_class import Address

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
    
    def get_name(self):
        return self.first_name + ' ' + self.last_name
