"""
========================================
 Band Name Generator
----------------------------------------
 A simple terminal-based Python program
 that asks the user two questions and
 generates a fun band name.

 Created in a clean, beginner-friendly
 style for GitHub and VS Code.
========================================
"""


def get_band_name():
    """

    Ask the user for inputs and return a generated band name.
    """


    print("🎵 Welcome to the Band Name Generator!\n")

    # First question
    city = input("What's the name of the city you grew up in? ").strip()

    # Second question
    pet = input("What's your pet's name? ").strip()

    # Create final band name
    band_name = f"{city} {pet}"

    return band_name


def main():

    """
    Main program runner.
    """

    result = get_band_name()

    print("\n Your band name could be: ✨✨", result,"✨✨")


# Run the program
if __name__ == "__main__":
    main()





# ====================================
# DEBUGGING EXAMPLES (commented out)
# ====================================

# Common mistake #1: forgetting to convert input type
# age = input("Enter your age: ")
# print(age + 5)   # ❌ TypeError: can only concatenate str to str

# Fix:
# age = int(input("Enter your age: "))
# print(age + 5)

# Common mistake #2: using a reserved keyword as variable name
# class = "Python"   # ❌ SyntaxError

# Common mistake #3: missing f-string or wrong concatenation
# print("Your band name is" + band_name)  # missing space before band_name

# Better: use f-strings (introduced later, but good to know)
# print(f"Your band name is {band_name}")


