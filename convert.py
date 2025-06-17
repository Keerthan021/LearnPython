ListOne = [1,2,3,4]
TupleOne = (1,2,3,4,5,6)
DictOne = {'Id':'123','Name':'Keerthan','Phone':'9495959393'}
SetOne = {1,3,56,66,54,4,333}

print("-----------------List------------------")
print(set(ListOne))
print(dict(enumerate(ListOne)))
print(tuple(ListOne))
print("-----------------Tuple-----------------")
print(list(TupleOne))
print(set(TupleOne))
print(dict(enumerate(TupleOne)))
print("---------------Dictionary--------------")
print(list(DictOne))
print(set(DictOne))
print(tuple(DictOne))
print("-----------------Set--------------------")
print(list(SetOne))
print(dict(enumerate(SetOne)))
print(tuple(SetOne))
print("---------------------------------------")