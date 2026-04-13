# Day 2: Tip Calculator & BMI Calculator

## What this project does
This folder contains two small Python programs:
- **Tip Calculator** – calculates how much each person should pay after adding a tip.
- **BMI Calculator** – calculates the Body Mass Index from weight and height.

## What I learned
- Working with floating-point numbers and rounding
- Using `input()` to get numbers from the user
- Converting strings to integers or floats (`int()`, `float()`)
- Arithmetic operators: `+`, `-`, `*`, `/`, `**` (exponent)
- f‑strings for clean output
- String indexing (in the quiz)

## How it works

### Tip Calculator
1. Asks for the total bill (float).
2. Asks for the tip percentage (10, 12, or 15).
3. Asks how many people will split the bill.
4. Calculates:  
   `(bill + bill * tip/100) / people`
5. Prints the amount each person pays, rounded to 2 decimal places.

### BMI Calculator
1. Uses fixed height = 1.65 m and weight = 84 kg (as given in the exercise).
2. Calculates BMI = weight / (height²).
3. Prints the result (exact value expected: `30.85399449035813`).

## Important notes
- `input()` always returns a string – convert to `int` or `float` before calculations.
- Division `/` always returns a float in Python.
- Use `**` for exponentiation: `height ** 2`.
- The tip calculator rounds down (`.2f` truncates/rounds to 2 decimals).

## Common mistakes
- Forgetting to convert the user input – causes `TypeError`.
- Using `height * height` instead of `height ** 2` (both work, but `**` is clearer).
- Not handling rounding – the result might show many decimals.

## Why this project matters
These programs introduce mathematical operations and user input handling – essential for any interactive application.

## ✨ Day 2 Highlights
- Tip calculator logic
- BMI formula implementation
- Understanding data types (int, float, string)
- Order of operations (PEMDAS)

---

# Day 2 Notes – Python Basics

## 1. Numeric Data Types
- `int` – whole numbers, e.g. `12`, `900`
- `float` – decimal numbers, e.g. `300.0`, `0.37`

## 2. Type Conversion
```python
int("5")      # string → integer
float("3.14") # string → float
str(123)      # number → string
```


## 3. Arithmetic Operators

| Operator | Meaning       | Example      |
|----------|---------------|--------------|
| `+`      | addition      | `6 + 4` → 10 |
| `-`      | subtraction   | `6 - 4` → 2  |
| `*`      | multiplication| `6 * 4` → 24 |
| `/`      | division      | `6 / 4` → 1.5|
| `**`     | exponent      | `2 ** 3` → 8 |
| `//`     | floor division| `7 // 3` → 2 |
| `%`      | modulus       | `7 % 3` → 1  |

## 4. Order of Operations (PEMDAS)

**P**arentheses → **E**xponents → **M**ultiplication/**D**ivision (left to right) → **A**ddition/**S**ubtraction (left to right).

## 5. Rounding

```python
round(0.37333, 2)   # → 0.37
f"{0.37333:.2f}"    # → "0.37"
```



---


# Quiz

Test your understanding of Python data types. Try to answer each question, then check the answers below.

---

### Question 1

What will the following code print?

```python
street_name = "Abbey Road"
print(street_name[4] + street_name[7])
```


- en

- ya

- eR

- yo

<details> <summary>✅ Explanation</summary>
String indexing starts at 0:
"Abbey Road" → indices:
0:A, 1:b, 2:b, 3:e, 4:y, 5: , 6:R, 7:o, 8:a, 9:d

street_name[4] = 'y'
street_name[7] = 'o'
Concatenation gives "yo".

</details>


---

### Question 2

What will this line of code print?

```python
print(6 + 4 / 2 - (1 * 2))
```

- 6.0

- 5

- 3

- 8.0

<details> <summary>✅ Explanation</summary>
Order of operations (PEMDAS):

Parentheses: (1 * 2) → 2

Division: 4 / 2 → 2.0 (float)

Addition & subtraction left to right: 6 + 2.0 → 8.0; 8.0 - 2 → 6.0

Because division produces a float, the final result is a float: 6.0.

</details>

---

### Question 3

What is the data type of the variable `a` after this code?

```python
a = int("5") / int(2.7)
```

- int

- float

- bool

- str

<details> <summary>✅ Explanation</summary>
int("5") → 5 (int)
int(2.7) → 2 (int truncates toward zero)
5 / 2 → 2.5 (float)

In Python, the / operator always returns a float, even if the result is a whole number.

</details>

---

### Question 4

Which of these lines of code will give an error?

- `name = input("What is your name?"); print(f"Hello, {name}")`
- `name = input("What is your name?"); print("Hello, " + name)`
- `age = 12; print(f"You are {age} years old")`
- `age = 12; print("You are " + age + " years old")`

<details>
<summary>✅ Explanation</summary>

The last line tries to concatenate a string (`"You are "`) with an integer (`age`) using `+`.  
Python does not automatically convert the integer – you must do it explicitly:

```python
print("You are " + str(age) + " years old")
```

The f-string version (third option) works because it converts automatically.

</details> 

---

### Question 5 

Which statement below is incorrect?

- `"523"` is a String
- `857.25` is a Float
- `"False"` is a Boolean
- `932` is an Integer

<details>
<summary>✅ Explanation</summary>

`"False"` with quotes is a string, not a boolean.  
Booleans in Python are written without quotes: `True` or `False`.

</details>

---

### Question 6

What is the data type of the variable `mystery`?

```python
mystery = 734_529.678
```

- String

- Qurtle

- Integer

- Float

<details> <summary>✅ Explanation</summary>
The underscore _ is allowed as a visual separator in numeric literals (ignored by Python).
The presence of a decimal point makes it a float.

</details> 

