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





    #Ask the user for inputs and return a generated band name.
print("🎵 Welcome to the Band Name Generator!\n")

    # First question
city = input("What's the name of the city you grew up in? ").strip()

    # Second question
pet = input("What's your pet's name? ").strip()

    # Create final band name
band_name = f"{city} {pet}"


print("\n Your band name could be: ✨✨", band_name,"✨✨")


