class classOne:
    def methodOne(self):
        print("This is method One")
    
    def methodTwo(self):
        print("This is method Two")

objOne = classOne()

objOne.methodOne()
objOne.methodTwo()
print('--------------------------------------')


class classOne:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def methodOne(abc):
        print(f"ID is {abc.id}\nName is {abc.name}\nEmail is{abc.email}")


objOne = classOne(123, 'Carter', 'carter@gmail.com')
objOne.methodOne()
print('--------------------------------------')


class myclass:
    @staticmethod
    def static(a, b):
        sum = a + b
        return sum
obj = myclass()
print(f'Sum is: {obj.static(10, 20)}')

print('--------------------------------------')

class myclass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    @property
    def display(self):
        sum = self.a + self.b
        return sum
    
obj = myclass(10, 20)
print(f' Propoerty method says Ans is: {obj.display}')
print('--------------------------------------')

class something:
    def __init__(self, name):
        self._name = name

    @property
    def setValue(self):
        return self._name
    
    @setValue.setter
    def setValue(self, value):
        if not value:
            raise ValueError("there is no value")
        self._name = value

s = something("Alice")
print(s.setValue)

s.setValue= "Bob"
print(s.setValue)

# s.setValue= ""