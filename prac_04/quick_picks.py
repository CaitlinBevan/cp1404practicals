"""Quick Pick Lottery Ticket Generator"""

import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
TOTAL_NUMBERS = 6

total_quick_picks = int(input("How many quick picks? "))
quick_picks = [0] * total_quick_picks
for i in range(total_quick_picks):
    for j in range(TOTAL_NUMBERS):
        results = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        print(f"{results:2.0f}", end=" ")
    print()
