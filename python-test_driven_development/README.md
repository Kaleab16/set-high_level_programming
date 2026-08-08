# Python - Test-Driven Development

This project covers writing Python functions using a test-driven
development (TDD) approach, including doctests embedded in function
docstrings and standalone `.txt` doctest files.

## Learning Objectives

* What's Unit testing and how to implement it in Python
* What's Test-driven development and how to implement it
* How to write a `.txt` file containing tests for a module and/or function
* How to use `doctest` to run those tests

## Requirements

* Editors allowed: `vi`, `vim`, `emacs`
* Files interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.9)
* All files end with a new line
* First line of all files: `#!/usr/bin/python3`
* Code follows `pycodestyle` (version 2.8.*)
* All modules, classes, and functions must have documentation
* All files must be executable

## Tasks

### 0. Integers Addition

**File:** `0-add_integer.py`, `tests/0-add_integer.txt`

Write a function that adds 2 integers.

* Prototype: `def add_integer(a, b=98):`
* `a` and `b` must be integers or floats, otherwise raises a `TypeError`
  with the message `a must be an integer` or `b must be an integer`
* `a` and `b` are cast to integers first if they are floats
* Returns an integer: the sum of `a` and `b`
* No imports allowed

**Run the tests:**

```bash
python3 -m doctest -v tests/0-add_integer.txt
```
