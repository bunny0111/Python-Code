#  Write a Python program to find the factorial of a number.


def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)


number = int(input("Enter the number="))
result = fact(number)
print(f"Factorial of {number} is {result}")
