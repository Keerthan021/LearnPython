def checkOccurance(list, value):
    count = 0
    for element in list:
        if element == value:
            count = count+1
    return count

list = [1,2,3,4,5,5,5,5,5,6,7,8,9]
value = 9
ans = checkOccurance(list, value)
print(f"Number of occurence of {value} is: {ans}")