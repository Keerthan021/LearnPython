class Parent:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
    
    def display(self):
        print(f'ID is: {self.id}\nName is:{self.name}\nEmail is: {self.email}')

class Child(Parent):
    def __init__(self, id, name, email, phone, address):
        super().__init__(id, name, email)
        self.phone = phone
        self.address = address
    
    def printData(self):
        print(f'Phone is: {self.phone}\nAddress is: {self.address}')

    @property
    def printAll(self):
        print(f'ID is: {self.id}\nName is:{self.name}\nEmail is: {self.email}\nPhone is: {self.phone}\nAddress is: {self.address}')

obj = Child(123, "Tony Stark", "tonystark@gmail.com", "9899888234", "New York, USA")
obj.display()
obj.printData()
print("------------------------------")
obj.printAll
