lists = [1, 2, 3, 4, 5]
my_dict = {"Id":"123", "Name": "Keerthan", "Phone":"8899001122"}
mySet = {"Apple", 1}
tuples = ('a', 'b', 'c', 1, 4, 5)

for list in lists:
    print(list)

print("\n")
#------------------------------------------
for key, value in my_dict.items():
    print(f"{key} : {value}")

print("\n")
#------------------------------------------
for i in mySet:
    print(i)

print("\n")
#------------------------------------------
for tuple in tuples:
    print(tuple)

print("\n")
#------------------------------------------

