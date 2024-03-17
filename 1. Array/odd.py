"""
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
"""

max_num = int(input("Enter Max Number= "))
odd_num = []

for i in range(1, max_num):
    if i % 2 == 1:
        odd_num.append(i)

print("Odd Number= ", odd_num)
