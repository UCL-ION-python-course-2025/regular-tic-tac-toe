# Helpful python concepts

This document contains potentially useful information for this game.

- Indexing lists
- Using **`.append()`** to modify lists
- Working with random.choice

---


## 📚 Lists and `.append()`

Lists store multiple items. You can add new items to the end of a list using the `.append()` method.

```python
fruits = ["apple", "banana"]
fruits.append("cherry")

print(fruits)  # ['apple', 'banana', 'cherry']
```

* `.append(item)` adds the `item` to the end of the list.
* It changes the list **in place** (it does not return a new list).

You can do this in a for loop to append multiple values to the end of the list

```python
numbers = []  # Empty list

for i in range(5):
    numbers.append(i)

print(numbers)  # [0, 1, 2, 3, 4]
```

---

## 🔢 Indexing into a List

In Python, you can access individual items in a list using **indexing**. Indexes start at **0**, not **1**!

### Example:

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # 'apple'
print(fruits[1])  # 'banana'
print(fruits[2])  # 'cherry'
```


### Common Mistake

Trying to access an index that doesn’t exist will cause an error:

```python
print(fruits[3])  # ❌ IndexError: list index out of range
```

### Tip

You can check the length of a list with `len()`:

```python
print(len(fruits))  # 3
```

This helps you avoid index errors when looping or slicing.

---


## 🎲 `random.choice`

The `random.choice()` function lets you pick a **random item** from a list.

### Example:

```python
import random

colors = ["red", "blue", "green", "yellow"]
chosen_color = random.choice(colors)

print("The chosen color is:", chosen_color)
```

Example output
```
The chosen color is: green
```

