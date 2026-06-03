# Day 7 Learning Rules

## Lists
A list stores multiple values in one variable.

```python
fruits = ["apple", "banana", "cherry"]
```

Random Choice

Pick one item from a list.

import random
word = random.choice(word_list)
Looping Through a String

You can check every letter in a word.

for letter in chosen_word:
    print(letter)
Enumerate

Use enumerate() to get both the index and the value.

for index, letter in enumerate(chosen_word):
    print(index, letter)
Conditionals

Use if, elif, and else to make decisions.

Game Logic

A Hangman game usually includes:

a secret word
a hidden display
lives
guessed letters
win or lose conditions

---

# `code_indentation_quiz.md`

# Code Indentation Quiz

## Question 1
Which version of code will output "This will run"?

```python
def my_function():
    print("This will run")

my_function()
```

Question 2

Which version of code will produce an Indentation Error when it is run?

def my_function():
print("Hello")
Question 3

In which version of code will you see "This will run" printed?

def my_function():
    a = 3
    if a > 2:
        print("This will run")

my_function()

---

# `001_Day_7_Goal_Click_Run_to_see_the_final_project.md`

# Day 7 Goal

Click Run to see the final Hangman project in action.
