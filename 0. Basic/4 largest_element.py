# Write a Python program to find the largest element in a list.


def largest_element(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


nums = [88, 76, 45, 208, 110]
largest_num = largest_element(nums)
print(f"The largest number is {largest_num}")
