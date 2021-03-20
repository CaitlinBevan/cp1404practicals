"""
CP1404/CP5632 - Practical
Random
"""

import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

#  What did you see on line 1?  6 and second run 6
#  What was the smallest number you could have seen, what was the largest?  5 and 20

#  What did you see on line 2?  7 and second run 9
#  What was the smallest number you could have seen, what was the largest? 3 and 9
#  Could line 2 have produced a 4? No, it will only show odd numbers up to and including 9.

#  What did you see on line 3?  4.901574805763684 and second run 2.690516754894262
#  What was the smallest number you could have seen, what was the largest? 2.5 and 5.5

#  Write code, not a comment, to produce a random number between 1 and 100 inclusive.

print(random.randint(1, 100))
