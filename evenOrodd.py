def checkit(para):
    result = []
    for element in para:
        if element % 2 == 0:
            result.append("Even")
        else:
            result.append("Odd")
    return result
Values = [1,2,3]
ans = checkit(Values)
print(ans)    