# def mergeName(firstName, lastName):
#     return firstName+" "+lastName
    

# firstName = "Keerthan"
# lastName = "Kumar"

# fullName = mergeName(firstName, lastName)
# print(fullName)


# def mergeName(firstName, lastName):
#     print(f"{firstName} {lastName}")

# firstName = "Keerthan"
# lastName = "Kumar"

# mergeName(firstName, lastName)

# elements = []
# print(elements)

# n = int(input("Enter the total number of elements: "))

# for i in range(n):
#     element = input(f"Enter element {i}: ")
#     elements.append(element)

# print(elements)

# for element in elements:
#     print(element)

# elements = []
# print("Enter items one by one. Type 'stop' to finish.")
# while True:
#     element = input("Enter the element: ")
    
#     if element.lower()== '':
#         break
#     elements.append(element)
# print(elements)

elements = set()
print("Add elements untill stop")

while True:
    element = input("enter the elements: ")
    if element.lower() == 'stop':
        break
    elements.add(element)
    print(elements)

for element in elements:
    print(element)