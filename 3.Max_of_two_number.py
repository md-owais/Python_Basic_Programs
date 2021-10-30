# Python program to find the
# maximum of two numbers
"""
# Logic
Input: a = 2, b = 4
Output: 4

Input: a = -1, b = -4
Output: -1

# Method-1: This is the naive approach
# where we will compare tow numbers using if-else statement and
# will print the output accordingly.
def maximum(a, b):
    if a >= b:
        return a
    else:
        return b
# Driver code
a = 10
b = 20
print(maximum(a, b))
"""

"""
# Method-2: Using max() function
# This function is used to find the maximum of the values passed as its arguments.
a = 20
b = 12

maximum = max(a, b)
print(maximum)
"""
"""
# Method-3: Using Ternary Operator
# This operator is also known as conditional expressions
# are operators that evaluate something based on a condition being true or false.
# It simply allows testing a condition in a single line.
# Driver code
a = 22
b = 24
# Use of ternary operator
print(a if a >= b else b)
"""

num1 = input("Enter the first number:\n")
num2 = input("Enter the first number:\n")
print(num1 if num1 >= num2 else num2)





