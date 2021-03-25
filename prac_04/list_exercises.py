#  1. Basic list operations
# total = 0
#
# numbers = [0] * 5
# print("Please enter 5 numbers")
# for i in range(5):
#     numbers[i] = int(input("Number: "))
#
# print(f"The first number is {numbers[0]}")
# print(f"The last number is {numbers[-1]}")
# print(f"The smallest number is {min(numbers)}")
# print(f"The largest number is {max(numbers)}")
#
# for number in numbers:
#     total += number
# average = total / len(numbers)
#
# print(f"The average of the numbers is {average}")


#  2. Woefully inadequate security checker

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
             'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface',
             'StartServer', 'bob']

username = input("Enter Username: ")
if username not in usernames:
    print("Access granted")
else:
    print("Access denied")
