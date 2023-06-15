def interchange(lists):
    # Swapping using third variable "temp"
    temp = lists[0]
    lists[0] = lists[len(lists) - 1]
    lists[len(lists) - 1] = temp

    return lists


numbers = [78, 45, 73, 24]
print("Before Swapping:", numbers)
print("After Swapping:", interchange(numbers))
