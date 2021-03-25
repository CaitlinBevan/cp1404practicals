"""Basic list operations"""
total = 0

numbers = [0] * 5
print("Please enter 5 numbers")
for i in range(5):
    numbers[i] = int(input("Number: "))

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")

for number in numbers:
    total += number
average = total / len(numbers)

print(f"The average of the numbers is {average}")
