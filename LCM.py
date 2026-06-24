import math
def LCM(n):
    """
    Write a program to find the smallest number divisible by all the numbers between 1 to n.
    """
    numbers = list(range(1,n+1))
    return math.lcm(*numbers)
n = int(input("Enter a number: "))
print(LCM(n))
