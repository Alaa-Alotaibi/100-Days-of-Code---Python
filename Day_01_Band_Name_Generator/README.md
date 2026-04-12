# Day 1: Band Name Generator

## What this project does
This program asks the user for two pieces of information and combines them to create a fun band name.

## What I learned
- How to use `input()`
- How to use `print()`
- How to store data in variables
- How to combine strings

## How it works
1. The program asks for the city name.
2. The program asks for the pet name.
3. It joins both answers together.
4. It prints the final band name.

## Important notes
- `input()` always gives a string.
- `strip()` removes extra spaces from the start and end of the text.
- `f-strings` make it easier to insert variables into text.

## Common mistakes
- Forgetting quotation marks around text
- Mixing up variable names
- Adding extra spaces in the output


## Why this project matters
This is a small but important first step because it teaches how to take user input and turn it into an output the program creates dynamically.

## ✨ Day 1 Highlights

#### Day 1 focused on:

- print statements
- debugging
- variables
- input()
- variable naming
- beginner logic
- building the Band Name Generator


---


# Day 1 Notes – Python Basics

## 1. Print Statements
- `print()` outputs text to the console.
- You can print strings: `print("Hello")`
- Print multiple items: `print("Hello", "World")` (automatically adds space)
- Escape sequences: `\n` new line, `\t` tab.

## 2. Debugging
Debugging is finding and fixing errors. Common beginner errors:
- **SyntaxError**: Misspelled keywords, missing quotes, wrong indentation.
- **TypeError**: Trying to combine different types (e.g., string + integer).
- **NameError**: Using a variable before defining it.

**Tip**: Read error messages carefully – they tell you the line number and what went wrong.

## 3. Variables
Variables store data. No need to declare a type – Python infers it.
```python
name = "Alice"      # string
age = 25            # integer
height = 5.8        # float
is_student = True   # boolean
