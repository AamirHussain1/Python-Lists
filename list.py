"""
 List methods:
 append(), extend(), pop(), remove(), insert(), sort(), sort(), sorted(), reverse(), clear(), del(),
 index(element) => output: index number of element, index[index number] => output: element itself,
 slice[], copy(), min(), max()
"""

lists = [12, "python", 1.2, 45, 78, 200]
print("original list:", lists)

# Append() will add a single element at the end
lists.append(13)
print("Appended list: ", lists)

new_list = ['django', 'flask', 100]

# extend() will add new list or number of elements different at once to the list
lists.extend(new_list)
print("extended list: ", lists)

# POP() will remove the element from its index
lists.pop(2)
print(lists)

# Remove() will delete the element from the list
lists.remove("python")
print(lists)

# insert() will add element at the given index number,
# rest of the elements after that will move to the next indices
lists.insert(9, 200)
print(lists)

# count() will count the occurrence of the given element passed as an argument
print(lists.count(200))

"""
 sort() will sort the list in ascending or descending order, but there is one drawback
 it will the sort the list only if datatype of all elements remains same because it cannot compare
 strings with integers or integers with complex numbers, it works only in case if all elements first converted
 to one datatype, same is the case with sorted() function 

 sort() : it is built in method used for lists 
 sorted() : it is built function in python used for any iterables
"""

# reverse() will reverse the list
lists.reverse()
print(lists)

"""
 For index, if element passes as an argument then use curly braces "()" and pass element to it,
 it will give index number of that element, in order to get the element at the index, use square braces "[]"
 it will give output as an element
"""
# index() will give the index number of the element passed as argument
print(lists.index(200))


# Negative index
print(lists[-4])

# positive index
print(lists[4])

"""
 slice() gives the range of elements, inside square braces uses slice operator with start point and ending point,
 including starting point, excluding ending point. Both positive and negative slicing is possible
 
"""
# Positive slice()
print(lists[0:5])

# Negative slice()
print(lists[-5: -1])

# copy() the original list
print(lists.copy())

"""
 clear() will clear entire list and gives the output a empty list
 del() will delete all the elements from list and throws error if try to print the list

"""
# lists.clear()
# print(lists)

# del lists
# print(lists) => throws error