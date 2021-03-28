"""Quick Pick Lottery Ticket Generator"""

import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
TOTAL_NUMBERS = 6

total_quick_picks = int(input("How many quick picks? "))
quick_picks = []
for i in range(total_quick_picks):
    for j in range(TOTAL_NUMBERS):
        result = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        quick_picks.append(result)
        quick_picks.sort()
        print(f"{result:2.0f}", end=" ")
    print()
# TODO: sort results
