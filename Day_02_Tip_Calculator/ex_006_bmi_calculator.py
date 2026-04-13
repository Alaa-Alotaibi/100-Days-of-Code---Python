
"""
EXERCISE 006 - BMI CALCULATOR

BMI = weight / height^2
This version takes input directly from the user.
"""

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / height ** 2

print(f"Your BMI is: {bmi:.2f}")
