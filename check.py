
# numberOne = input("Enter the first number: ")
# numberTwo = input("Enter the second number: ")


# if numberOne == numberTwo:
#     print("Numbers are equal")

# elif numberOne > numberTwo:
#     print("Number 1 is greater than Number 2")

# elif numberTwo > numberOne:
#     print("Number 2 is greater than Number 1")
# try:
#     ans = 10/0
#     print(ans)
# except ZeroDivisionError:
#     print("Cant")
# else:
#     print("cantt")
# finally:
#     print("don't worry")
class parent:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def display(self):
        print(f"Name is: {self.name} And phone is: {self.phone}")

c = parent("Alice", 123)
c.display()