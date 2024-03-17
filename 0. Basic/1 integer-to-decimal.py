# 1. Converting an Integer into Decimals


def integer_to_decimal(int_value):
    decimal_place = 2  # specify as per the requirement
    divisor = 10**decimal_place
    print(type(divisor))
    return int_value / divisor


int_value = int(input("Enter integer value="))
print("Integer value=", int_value)
dec_value = integer_to_decimal(int_value)
print(dec_value)
