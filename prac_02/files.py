"""
CP1404/CP5632 - Practical
Files
"""

#  1.  Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.

# name = input("What is your name? ")
# out_file = open("name.txt", "w")
# print(name, file=out_file)
# out_file.close()

#  2.  Write code that opens "name.txt" and reads the name (as above) then prints,
#  "Your name is Bob" (or whatever the name is in the file).

# in_file = open("name.txt", "r")
# file_contents = in_file.read()
# in_file.close()
# print(f"Your name is {file_contents}")

#  3.  Create a text file called numbers.txt and save it in your prac_02 directory.

# out_file = open("numbers.txt", "w")
# out_file.write("17\n")
# out_file.write("42\n")
# out_file.write("400\n")
# out_file.close()
#
# in_file = open("numbers.txt", "r")
# line1 = int(in_file.readline())
# line2 = int(in_file.readline())
# in_file.close()
#
# total = line1 + line2
# print(f"The total of line 1 and line 2 is {total}")


# 4.  Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number
# of numbers.

total = 0

in_file = open("numbers.txt", "r")
for line in in_file:
    total += int(line)
in_file.close()
print(total)

