def main():
    """Get user's score and display result."""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    get_result(score)
    print(f"Your score of {score} is {get_result(score)}")


def get_result(score):
    """Return result category."""
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    else:
        return "Excellent"


main()
