# Write a Python program to check if a string is a palindrome.


def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string


word = input("Enter the word=")

if is_palindrome(word):
    print(f"{word} is palindrome")
else:
    print(f"{word} is not palindrome")
