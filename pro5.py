#Append to the list, Remove, Pop
# my_list = [1,2,2,3,3,4]

# while True:
#     element = input("Enter the element: ")
#     my_list.append(element)
#     if element.lower() == "":
#         break
#     print(my_list)
# my_list.remove(2)
# print(my_list)
# my_list.pop(5)
# print(my_list)
# list = [1,2,3,4,5,6]
# for i in list:
#     square = i*i
#     print(square)
# print([i**2 for i in list])

# listEven = [1,2,3,4,5,6]

# print([i for i in listEven if i%2 == 0 ])

# listName = ["Keerthan"]
# for i in listName[0]:
#     l = listName[i]
   
#     print([i])
#print([char for char in listName[0]])

# listName = ["Keerthan"]
# print([char for char in listName[0]])

# listName = ["Keerthan"]
# vowels = "aeiouAEIOU"
# print([char for char in listName[0] if char in vowels ])

# print([char for char in listName[0].lower() if char in 'aeiou'])

# listName = ["Keerthan","Alice"]
# vowel = []
# for i in listName:
#     for j in i:
#         if j in 'aeiou':
#             vowel.append(j)
# print(vowel)

# print([char for char in listName[1].lower() if char in 'aeiou'])

#     name = listName[i]

#     nameLower = name.lower()

#     vowel = []
#     for char in nameLower:
#         if char in 'aeiou':
#             vowel.append(char)
# print(vowel)

# print([char for char in listName[0].lower() if char in 'aeiou'])

listName = ["Keerthan", "Alice"]
print([char for name in listName for char in name if char in 'aeiou'])

print([val for val in range(11, 1, -2) ])