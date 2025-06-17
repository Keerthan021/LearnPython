# #positional
# def positional(numberOne, numberTwo):
#     ans = numberOne + numberTwo
#     return ans
# print(positional(10, 20))

# #keyword 
# print("-------------------------------------------")

# def keyword(numberOne, numberTwo):
#     ans = numberOne + numberTwo
#     return ans
# print(keyword(numberOne=10, numberTwo=20))

# print("-------------------------------------------")

# #default arguments
# def default(name, age= 20, gender = 'Male'):
#     print(f"The Name is {name}, Age is {age}, gender is {gender}")

# default('Alice', 24, 'Female')
# default('Aman',10)
# default('Arjun',gender='Male')
# print("-------------------------------------------")
# #Variable length positional
# def variableLength(*Values):
#     print(sum(Values))

# variableLength(1)
# variableLength(2,2,2,2)
# variableLength(10,20,30,40)
# print("-------------------------------------------")

# #variable length keyword arguments

# def keywordArguments(**infos):
#     for key, value in infos.items():
#         print(f"{key}:{value}")


# keywordArguments(Name= 'Keerthan', Age= 18, Phone = 9900223344)
# print("-------------------------------------------")

# # Keyword-Only Arguments
# def keywordOnlyArgs(kArgName,*,kArgAge):
#     print(f"{kArgName} {kArgAge}")

# keywordOnlyArgs('Keerthan',kArgAge=10)
# keywordOnlyArgs('Tony',kArgAge=20)
# print("-------------------------------------------")
# matrix = [1,2,3,4,5,6]
# result = []
# print([char for item1 in matrix for char in matrix])
# for i in matrix:
#     for j in matrix:
#         result.append(j)
# print(result)

listOne = [0,1,2,3,4,5,6,7,8,9]
try:
    for element in listOne:
        print(element / 0)
        
except IndexError:
    print("out of bound")

except ZeroDivisionError:
    print("cant divide")