"""Basic list operations"""


numbers = [0] * 5
print("Please enter 5 numbers")
for i in range(5):
    numbers[i] = int(input("Number: "))
print(numbers)
