# Day 5 Learning Rules

## Loops

A loop allows code to repeat multiple times.

### For Loop

```python
for item in items:
    print(item)
```

---

## Range Function

```python
for number in range(1, 11):
    print(number)
```

Produces:

1 2 3 4 5 6 7 8 9 10

---

## Summation Pattern

```python
total = 0

for number in range(1, 101):
    total += number
```

---

## Finding Maximum Values

```python
highest = 0

for score in scores:
    if score > highest:
        highest = score
```

---

## FizzBuzz Logic

- Divisible by 3 → Fizz
- Divisible by 5 → Buzz
- Divisible by both → FizzBuzz

---

## Password Generator Concepts

- Lists
- Loops
- Random module
- Shuffle
- String building
