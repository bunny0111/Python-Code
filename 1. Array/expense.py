"""
Let us say your expense for every month are listed below,
i. January = 2200
ii. February = 2350
iii. March = 2600
iv. April = 2130
v. May = 2190

Create a list to store these monthly expenses and using that find out,
1. In Feb, how many dollars you spend extra compare to Jan?
2. Find out your total expense in first quarter (Jan, Feb, March) of the year?
3. Find out if you spent exactly 2000 dollar in any month?
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this?
"""

expense_list = [2200, 2350, 2600, 2130, 2190]
print(expense_list)

# Solutions

print("In Feb, how many dollars you spend extra compare to Jan:")
diff = expense_list[1] - expense_list[0]
print("$", diff)

print("Find out your total expense in first quarter (Jan, Feb, March) of the year?")
total_exp = expense_list[0] + expense_list[1] + expense_list[2]
print("$", total_exp)

print("Find out if you spent exactly 2000 dollar in any month?")
find = 2000 in expense_list
print(find)

print(
    "June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list"
)
expense_list.append(1980)
print(expense_list)

print(
    "You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this?"
)
April_new_bill = expense_list[3] - 200
print(April_new_bill)
