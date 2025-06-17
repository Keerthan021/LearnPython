Elements = [12, 35, 66666, 568934, 1, 4, 0, 2, 7, 5, 100, -10, 20, 25]
my_list = ['id','name','phone','contact']
sorted_elements = sorted(Elements)
print(sorted_elements)
print("--------------------------------------------------")
print(len(Elements))
print("--------------------------------------------------")
print(sum(Elements))
print("--------------------------------------------------")
print(min(Elements))
print("--------------------------------------------------")
print(max(Elements))
print("--------------------------------------------------")
for index, Value in enumerate(Elements):
    print(index, Value)
print("--------------------------------------------------")
zipped = zip(Elements, my_list)
print(list(zipped))
print("--------------------------------------------------")
values = [0, False, 5, None]
anyValues = any(values)
print(anyValues)
print("--------------------------------------------------")
numbers = [1,2,3,4,5,6,7]
square = map(lambda x:x**2, numbers )
print(list(square))
print("--------------------------------------------------")
numbersTwo = [2,3,4,5,6,7,8,9,0]
even = filter(lambda x: x%2 == 0, numbersTwo)
print(list(even))
print("--------------------------------------------------")
square = lambda x: x*2
print(square(4))

print("--------------------Set----------------")
setOne = {1, 12, 9009, -12, 0, 2, 3, 4, 45, 43, 18, 24 , 6, 7}
sortedSet = sorted(setOne)
print(sortedSet)
print("--------------------------------------------------")
print(max(setOne))
print("--------------------------------------------------")
print(min(setOne))
print("--------------------------------------------------")
print(any(setOne))
print("--------------------------------------------------")
print(all(setOne))
print("--------------------------------------------------")

setTwo = setOne.copy()
print(setTwo) 
print("--------------------------------------------------")
a = {1,2,3,4,4}
b = {2,3,5}
c = {1,2,3}
d = {37,65}

print(a.union(b))
print("--------------------------------------------------")
print(a.intersection(b))
print("--------------------------------------------------")
print(a.difference(b))
print("--------------------------------------------------")
print(b.difference(a))
print("--------------------------------------------------")
print(a.symmetric_difference(b))
print("--------------------------------------------------")
print(a.issubset(c))
print("--------------------------------------------------")
print(a.issuperset(c))
print("--------------------------------------------------")
print(a.isdisjoint(d)) 

print("-------------dictionary------------")

dictionary = {'id':123,'name':'Lenovo', 'phone':'9988776655'}
print(dictionary.get('id'))
print("--------------------------------------------------")
print(dictionary.get('name'))
print("--------------------------------------------------")
print(dictionary.get('key'))
print("--------------------------------------------------")

print(dictionary.keys())
print("--------------------------------------------------")
print(dictionary.values())
print("--------------------------------------------------")
for key, value in dictionary.items():
    print(key,value)
print("--------------------------------------------------")
print(dictionary.popitem())
print("--------------------------------------------------")
dictionary.update({'Address':'Bejai, Manglore', 'state':'Karnataka', 'pin':'575001'})
print(dictionary)

dictionary.setdefault('gender','Male')
print(dictionary)

keys = ['id','name','phone']
print(dictionary.fromkeys(keys, 0))

print("---------Tuple--------")
tupleOne = (1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,4,5)
print(min(tupleOne))
print(max(tupleOne))
print(sum(tupleOne))
print(tupleOne.count(2))
print(sorted(tupleOne))