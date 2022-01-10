# Find Factorial of a given numbers
# Logic
# n! = n*(n-1)*(n-2)*....*1
# Example:
# 4! = 4*3*2*1 = 24
'''
def factorial(n):
# Single line to find factorial
    return 1 if(n==1 or n==0) else n*factorial(n-1);
num = 5;
print("Factorial of",num,"is",factorial(num))
'''
"""
# 2.Iterative
def factorial(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        fact=1
        while(n>1):
            fact *=n
            n -=1
        return fact
num = 5;
print("Factorial of",num,"is",factorial(num))
"""
# 3.Factorial Using In-Built Method
import math
def  factorial(n):
    return(math.factorial(n))
num = 4;
print("Factorial of",num,"is",factorial(num))