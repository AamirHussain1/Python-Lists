lists = [12, 78, 23, 78, 12]

count = 0
element = int(input("Enter element: "))

for num in lists:
    if num == element:
        count += 1
print(count)
