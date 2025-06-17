# def sum():
#     print("Hello")

# class sample:
#     def justMethod(self):
#         print("Hi")
# sum()
# a = sample()
# a.justMethod()
# stringOne = "Hello"
# stringTwo = "hi"
# stringThree = "Hello"


# print(stringOne == stringTwo)
# print(stringOne == stringThree)

# print(stringOne.lower() == stringOne.upper())

# print('apple'>'BANANA')
# print('APPLE'=='apple')

# print('mostly cloudy' == 'Raining')
# print('mostly cloudy' == 'Mostly cloudy')

message = "   Hello  "
print(message)

print(message.lstrip())
print(message.rstrip())
print(message.strip())

message = "Hello World"
print(message.find("d"))
print(message.index("W"))

print(message.replace("Hello", "Hellooo!"))
print(len(message))
print(message.count('l'))

print(message.startswith("H"))
print(message.startswith("W"))
print(message.endswith("d"))
print(message.endswith("!"))

message = 'a,b,c,d,e,f'
print(message.split(','))