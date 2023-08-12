import math

def is_perfect_square(number):
    s = int(math.sqrt(number))
    return s * s == number

def is_fibonacci(number):
    if is_perfect_square(5 * (number ** 2) + 4) or is_perfect_square(5 * (number ** 2) - 4):
        return True
    else:
        return False

num = int(input("Enter number to check: "))
if is_fibonacci(num):
    print(f"{num} is a Fibonacci number.")
else:
    print(f"{num} is not a Fibonacci number.")
