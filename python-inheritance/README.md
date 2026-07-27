# Python - Inheritance

This project covers inheritance in Python, including class inheritance, method overriding, and attribute lookup.

## Files

| File | Description |
|------|-------------|
| `0-lookup.py` | Function that returns the list of available attributes and methods of an object |

## Requirements

- Python 3.8.5
- Ubuntu 20.04 LTS
- All files should end with a new line
- Code style: PEP 8 (pycodestyle)

## Usage

```python
lookup = __import__('0-lookup').lookup

class MyClass:
    pass

print(lookup(MyClass))
