# 🏝️ Day 3: Treasure Island

## What this project does
This project is a text-based adventure game where the player makes choices to find hidden treasure.

The game uses **nested conditional statements** to control the story path based on the player's decisions.

The player must:
- choose left or right
- decide whether to wait or swim
- choose the correct door color

Only one path leads to winning the treasure.

---

## What I learned
- how to use `if`, `elif`, and `else`
- nested conditional statements
- logical thinking with branching paths
- using `.lower()` to make input case-insensitive
- converting flowcharts into Python logic
- how decision trees work in programming
- how multiple choices create different outcomes

---

## How it works
1. The player starts at a crossroads.
2. Choosing **left** continues the game.
3. Choosing **right** ends the game.
4. The second choice is **wait** or **swim**.
5. Waiting safely reaches the island.
6. The final choice is a colored door.
7. Choosing **yellow** wins the game.

---

## Important notes
- `.lower()` helps standardize user input.
- Nested `if` statements are useful for multi-step decisions.
- Flowcharts make it easier to plan game logic.
- Every branch should have a clear ending.
- Always handle invalid choices when possible.

---

## Common mistakes
- forgetting `.lower()` on user input
- wrong indentation inside nested `if`
- using `=` instead of `==`
- missing `else` branches
- placing `elif` under the wrong block
- forgetting to cover invalid door names

---

## Why this project matters
This project is one of the first real examples of **programming logic and decision trees**.

It teaches how real programs:
- respond to user choices
- follow different paths
- end with different outcomes
- use structured control flow

This is the foundation of:
- games
- apps
- chatbots
- automation logic
- AI decision systems

---

# ✨ Day 3 Highlights
Day 3 focused on:

- `if`
- `elif`
- `else`
- nested conditionals
- logical operators
- flowcharts
- Treasure Island game
- BMI interpretation
- ticket pricing logic

---
## 🧠 Day 3 Notes – Control Flow and Logical Operators

### 1) Basic if / else
Used when the program needs to make **one decision**.

```python
age = 18

if age >= 18:
    print("Can ride")
else:
    print("Can't ride")
```

---

### 2) if / elif / else
Used when there are **multiple conditions**.

```python
if bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("underweight")
```

---

### 3) Nested if Statements
Used when **one condition depends on another**.

```python
if choice1 == "left":
    if choice2 == "wait":
        print("Continue")
```

Treasure Island uses this heavily because every next choice depends on the previous one.

---

### 4) Logical Operators
Python supports:

- `and`
- `or`
- `not`

#### Examples
```python
True or False
True and False
not True
```

These help combine multiple conditions in one statement.

---

## 🎮 Treasure Island Logic Map
The game logic follows this path:

- `left` → continue
- `right` → game over
- `wait` → continue
- `swim` → game over
- `yellow` → win
- `red` / `blue` → game over

This logic was first planned using the **Treasure Island flowchart**, which made it much easier to convert into Python code.

---

## 📊 BMI Calculator with Interpretation
This exercise introduced **multi-condition decision logic**.

```python
weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("underweight")
```

### What this teaches
- condition ordering matters
- `elif` prevents unnecessary checks
- ranges are easier with ordered logic
- control flow should go from highest condition to lowest

---

## 🎟️ Ticketing Flowchart Practice
This exercise helped translate **visual flowcharts into real code logic**.

### Logic
- if `height < 120` → cannot ride
- else → ask age
- child → `$5`
- teen → `$7`
- adult → `$12`
- photo option → extra `$3`

This is the beginning of **real-world pricing and business rule logic systems**.

---

## 🧠 Logical Operators Quiz

### Question 1
What does this evaluate to?

```python
False or True or False
```

✅ **Answer:** `True`

---

### Question 2
What will this print?

```python
a = 5
b = 7

if a >= b and a != b:
    print("A")
elif not a >= b and a != b:
    print("B")
else:
    print("C")
```

✅ **Answer:** `B`

---

### Question 3
What does this evaluate to?

```python
not 5 == 5
```

✅ **Answer:** `False`

---

## 🧩 Flowchart Thinking Notes
Today’s most important skill was:

> **turning flowcharts into code**

### Best way to solve condition problems
1. draw the decisions
2. split outcomes into branches
3. convert each branch into `if`
4. nest where needed
5. test every possible route

This is a **core software engineering skill** because almost every app, game, API, and automation script depends on decision trees.
