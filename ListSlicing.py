#List slicing, basic, negative index, with step
my_list = ['a','b','c','d','e','f','g','h']

print(my_list[0:1:])
print(my_list[0:7:])
print(my_list[2:6:])
print(my_list[1:6:])
print(my_list[5:8:])
print(my_list[0:0:-1])

print("-----------------------")

print(my_list[1:8:2])
print(my_list[8:0:-2])
print(my_list[0::2])
print(my_list[1::])
print(my_list[::])