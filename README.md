# Password Validator Testing - README

## Overview
This project is focused on generating and testing passwords using Finite Automata (DFA/NFA) approaches. The goal is to evaluate each method's performance,
accuracy, and extensibility. Additionally, sets of test passwords have been created to simulate
various real-world scenarios.

## Contents

### `varied_passwords.txt`
- Contains 100 randomly generated passwords of varied lengths and character types.
- Designed to test:
  - Presence of uppercase letters
  - Presence of lowercase letters
  - Presence of digits
  - Presence of special characters
  - Presence of **invalid** characters (e.g., spaces, backslashes, quotes)
  - Passwords with length below and above 8 characters

## Requirements
- Python 3.11+
- No external libraries required

## How to Use
1. Load and parse the password files using Python:
```python
with open("varied_passwords.txt") as f:
    passwords = [line.strip() for line in f]
```

2. Use password validators (DFA, NFA) to classify each password.

3. Measure performance using `time` or `timeit`.

## Notes
- The DFA encodes state transitions for all combinations of character type requirements.
- The NFA runs four parallel automata, each checking one requirement.

## Author
Fiesta89
