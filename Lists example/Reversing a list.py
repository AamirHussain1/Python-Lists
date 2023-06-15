def reverse(lists):
    # Using built in method reverse() method
    # lists.reverse()

    reversed_list = lists[::-1]

    return reversed_list


numbers = [89, 23, "python", 56, 78]
print(reverse(numbers))
