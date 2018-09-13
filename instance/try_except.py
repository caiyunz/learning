#!/usr/bin/python3
print("Please input the two number!")
print("If two number's sum is 0 to exit.")
while 1:
    try:
        first_number=input("Please input the first number:")
        second_number=input("Please input the second number:")
        number=int(first_number)+int(second_number)
    except ValueError:
        print("Please input int number instead of character.")
    else:
        print(str(number))
        if int(number) == 0:
            break
