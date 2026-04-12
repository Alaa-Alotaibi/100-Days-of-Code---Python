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
```

---


## 🧠 Variable Naming Quiz

**Score: 0.00 of null%** | **Correct: 0** | **Incorrect: 0**

Test your understanding of Python variable naming rules. Try to answer each question, then check the answers below.

---

### Question 1

Which line of Python code is valid?

- `a = 12`
- `a: 12`
- `var a = 12`
- `12 = a`

<details>
<summary>✅ Answer</summary>

**`a = 12`** – This is a valid assignment statement.  
The others are invalid because:
- `a: 12` uses a colon instead of `=`
- `var a = 12` is JavaScript syntax, not Python
- `12 = a` cannot assign to a literal number
</details>

---

### Question 2

Which block of code will produce an error? For extra points, which type of error do you think it will produce?

**Option A**
```python
time_until_midnight = "5"
print("There are " + time_until_Midnight + " hours until midnight")
```

**Option B**
```python
time_until_midnight = "5"
print("There are " + time_until_midnight + " hours until midnight")
```

**Option C**
```python
num_hours = "5"
print("There are " + num_hours + " hours until midnight")
```

<details> <summary>✅ Answer</summary>

Option A produces a NameError because the variable inside print() is time_until_Midnight (capital M), but the defined variable is time_until_midnight (lowercase m). Python variable names are case‑sensitive.

Options B and C are correct and will run without errors.

</details>


### Question 3

Which is the **best** variable name for Player 1's username?

- `1_player_username = "jackbauer"`
- `player1_username = "jackbauer"`
- `p1 user name = "jackbauer"`
- `p1u = "jackbauer"`

<details>
<summary>✅ Answer</summary>

**`player1_username = "jackbauer"`** is the best variable name because it is descriptive, valid (starts with a letter, no spaces), and follows snake_case convention.  
- `1_player_username` – starts with a digit (invalid)  
- `p1 user name` – contains spaces (invalid)  
- `p1u` – valid but not descriptive; poor readability

</details>

