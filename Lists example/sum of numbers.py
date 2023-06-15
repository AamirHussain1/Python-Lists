# Function that calculates the returns the sum
def sum_of_numbers(numbers):
    total_sum = 0
    """
    "range()" method when applies on iterators without "len()" function, it throws because 
    range functions is used for generating numbers
    """
    for nums in range(len(numbers)):
        total_sum = total_sum + numbers[nums]

    return total_sum


lists = [34, 89, 76, 56]
print("Sum of all elements: ", sum_of_numbers(lists))
