def remove_duplicates(numbers):
    # Empty list to store unique elements
    new_list = []

    for nums in numbers:
        # checks whether the element is present in the empty list, if not, it appends that to the list
        if nums not in new_list:
            new_list.append(nums)

    return new_list


lists = [45, 45, 45, 67, 67, 66, 66, 67, 66, 98, 34, 67, "python", "python"]
print("New list after removing Duplicates:", remove_duplicates(lists))

# Using built-in method
new_lists = set(lists)
print(list(new_lists))
