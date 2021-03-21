import random


def main():
    """Get user's score and display result."""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    get_result(score)
    print(f"Your score of {score} is {get_result(score)}")
    random_score = random.randint(0, 100)
    print(f"Your randomly generated score of {random_score} is {get_result(random_score)}")


def get_result(score):
    """Return result category."""
    if score < 50:
        return "Bad"
    elif score < 90:
        return "a Pass"
    else:
        return "Excellent"


main()
