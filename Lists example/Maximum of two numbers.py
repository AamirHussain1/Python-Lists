number_1 = int(input("Enter 1st Number: "))
number_2 = int(input("Enter 2nd Number: "))

# Using built in method max()
print("Using built in method, Maximum is", max(number_1, number_2))

# Using conditional statement
if number_1 > number_2:
    print("Maximum is ", number_1)

elif number_2 > number_1:
    print("Maximum is ", number_2)

elif number_1 == number_2:
    print("Both numbers are equal")

else:
    print("Enter valid integer")
