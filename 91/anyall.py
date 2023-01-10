import re
VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    return all(char in VOWELS for char in input_str.lower())


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    return re.search(rf'[{PYTHON}]', input_str.lower())


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    return re.search(r'\d+', input_str)