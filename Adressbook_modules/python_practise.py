class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def _protected_method(self):
        print("protected method")
    def __private_method(self):
        print("privated method")

if __name__ == "__main__":
    p = Person("mohan", 23)
    #p._protected_method() 
    #p.__private_method() 

    print(Person.__dict__)