import math
def maxmin(a, b):
    return max(a, b), min(a, b)
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))   
print("Maximum number is:", maxmin(a, b)[0])
print("Minimum number is:", maxmin(a, b)[1])