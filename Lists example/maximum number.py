def maximum_number(numbers):
    # Assuming max number is at index 0
    max_number = numbers[0]

    # iterating over numbers to compare all elements with max_number
    for nums in numbers:
        if nums > max_number:
            max_number = nums

    return max_number


lists = [12, 78, 98, 54]
print("Maximum number is:", maximum_number(lists))

# using built-in method
print(max(lists))
