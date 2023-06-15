def find(lists):
    element = int(input("Enter the num you want to find: "))
    for nums in numbers:
        if element in numbers:
            return lists.index(element)

        else:
            return False


numbers = [45, 78, 98, 23]

print("Element found at position", find(numbers))
