"""Quick Pick Lottery Ticket Generator"""

import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
TOTAL_NUMBERS = 6

total_quick_picks = int(input("How many quick picks? "))
for i in range(total_quick_picks):
    quick_picks = []
    for j in range(TOTAL_NUMBERS):
        random_quick_pick = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while random_quick_pick in quick_picks:
            random_quick_pick = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        quick_picks.append(random_quick_pick)
    quick_picks.sort()
    print("".join("{:2}".format(quick_pick) for quick_pick in quick_picks))
