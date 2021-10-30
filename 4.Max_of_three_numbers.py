# Python program maximum of three
# Logic
# Input : a = 2, b = 4, c = 3
# Output : 4
#
# Input : a = 4, b = 2, c = 6
# Output : 6
"""
# Method-1(Simple):
# Python program to find the largest
# number among the three numbers
def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a

    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    return largest
# Driven code
a = 10
b = 14
c = 12
print(maximum(a, b, c))
"""

"""
# Method-2 (Using List):
# . Initialize three number by n1, n2 and n3
# . Add three numbers into list lst = [n1, n2, n3].
# . Using max() function to find the greatest number max(lst).
# . And finally we will print maximum number
# Python program to find the largest number
# among the three numbers using library function

def maximum(a, b, c):
	list = [a, b, c]
	return max(list)

# Driven code
a = 10
b = 14
c = 12
print(maximum(a, b, c))
"""

# Method-3(Using max function)
# Python program to find the largest number
# among the  three numbers using library function
# Driven code
a = 10
b = 14
c = 12
print(max(a, b, c))
