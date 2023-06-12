lists = [12, 67, 90, 45]

for i in range(1, len(lists)):
    if lists[i] < lists[i - 1]:
        print(True)

    else:
        print(False)
