def swap(numbers, first_number, second_number):
    position_1 = numbers.index(first_number)
    position_2 = numbers.index(second_number)

    temp = numbers[position_1]
    numbers[position_1] = numbers[position_2]
    numbers[position_2] = temp

    return numbers


lists = [56, 78, 34, 68]
print("Original list: ", lists)
first_no = int(input("Enter First number: "))
second_no = int(input("Enter second number: "))

print("Swapped List", swap(lists, first_no, second_no))
