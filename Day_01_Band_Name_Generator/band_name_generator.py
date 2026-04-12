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