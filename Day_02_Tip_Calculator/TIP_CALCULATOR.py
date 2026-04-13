"""
DAY 2 PROJECT - TIP CALCULATOR

This program calculates how much each person should pay
after splitting the bill and adding a tip.
"""


def calculate_tip():
    print("💸 Welcome to the tip calculator!\n")

    bill = float(input("What was the total bill? $"))
    tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill? "))

    total_with_tip = bill * (1 + tip_percent / 100)
    amount_per_person = round(total_with_tip / people, 2)

    print(f"\nEach person should pay: ${amount_per_person:.2f}")


if __name__ == "__main__":
    calculate_tip()