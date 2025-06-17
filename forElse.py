numbers = [1, 3, 5, 7]

for num in numbers:
    if num % 2 == 0:
        print("Found an even number:", num)
        break

print("No even number found.")

numbers = [1, 3, 5, 7]

for num in numbers:
    if num % 2 == 0:
        print("Found an even number:", num)
        break
else:
    print("No even number found.")
