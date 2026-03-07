"""
In this assignment I will do factorial using loop and recursive function.
"""

def while_factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        while n > 1:
            fact *=  n
            n -= 1
        return fact

def for_factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact

def rec_factorial(n):
    if n == 0:
        return 1
    else:
        return n * rec_factorial(n-1)


from math import factorial

# Taking number from user:
n = int(input("Enter a number for which factorial to be calculated: "))
print(f"Factorial of {n} using while loop {while_factorial(n)}")
print(f"Factorial of {n} using for loop {for_factorial(n)}")
print(f"Factorial of {n} using recursive function {rec_factorial(n)}")
print(f"Factorial of {n} using factorial function from math module {factorial(n)}")
