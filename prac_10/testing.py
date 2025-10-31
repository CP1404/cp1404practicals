"""
CP1404/CP5632 Practical
Testing code using assert and doctest
Estimate: 20 min
Actual: 19 min
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between.
    >>> repeat_string("hi", 2)
    'hi hi'
    >>> repeat_string("Python", 1)
    'Python'
    >>> repeat_string("x", 0)
    ''
    """
    if n <= 0:
        return ""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in.
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def sentence_case(phrase: str) -> str:
    """
    Return the phrase as a proper sentence: capitalised and ending with a single full stop.

    Rules:
    - Leading/trailing whitespace is removed.
    - First character is upper-cased (if present).
    - Exactly one full stop is ensured at the end (no double punctuation).

    >>> sentence_case('hello')
    'Hello.'
    >>> sentence_case('It is an ex parrot.')
    'It is an ex parrot.'
    >>> sentence_case('  multiple   spaces here  ')
    'Multiple   spaces here.'
    """
    phrase = phrase.strip()
    if not phrase:
        return "."  # minimal sentence
    # Capitalise first character only; keep rest as-is to avoid changing acronyms
    phrase = phrase[0].upper() + phrase[1:]
    # Remove trailing punctuation dots
    while phrase.endswith("."):
        phrase = phrase[:-1]
    return phrase + "."


def run_tests():
    """Run the tests on the functions with basic assert tests."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should now pass
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # TODO: 2. write assert statements to show if Car sets the fuel correctly
    # Test default fuel (should be 0)
    default_car = Car()
    assert default_car.fuel == 0, "Default fuel should be 0"
    # Test provided fuel value
    ten_fuel_car = Car(fuel=10)
    assert ten_fuel_car.fuel == 10, "Fuel should be set from constructor argument"


run_tests()

# TODO: 3. Uncomment the following line and run the doctests
# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()
