"""
CP1404/CP5632 Practical
Recursion
Estimate: 10 min
Actual: 28 min
"""


def do_it(n):
    """Return the count of odd numbers from 1..n (inclusive) using recursion."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO: 1. write down what you think the output of this will be,
# TODO: 2. use the debugger to step through and see what's actually happening
# Expected for do_it(5): 3 (the odds are 1,3,5)
print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0 (inclusive)."""
    if n < 0:
        return
    print(n ** 2)
    do_something(n - 1)


# TODO: 3. write down what you think the output of do_something(4) will be,
# TODO: 4. use the debugger to step through and see what's actually happening
# do_something(4)


# TODO: 5. A backwards version: print on the way back out
def do_something_backwards(n):
    """Recursively print the squares from 0 up to n (inclusive)."""
    if n < 0:
        return
    do_something_backwards(n - 1)
    print(n ** 2)


# ---- Pyramid program ----
def blocks_loop(rows: int) -> int:
    """Return the number of blocks for a 2D pyramid using a loop.
    e.g., for 6 -> 21
    """
    total = 0
    for i in range(1, rows + 1):
        total += i
    return total


def blocks_recursive(rows: int) -> int:
    """Return the number of blocks for a 2D pyramid using recursion."""
    if rows <= 0:
        return 0
    return rows + blocks_recursive(rows - 1)


# ---- Other recursive challenges ----
def outside_in(s: str) -> str:
    """Return a string printed from the outside in (space-separated).
    Example: "Programming" -> "P g r n o i g m r m a"
    """
    if not s:
        return ""
    if len(s) == 1:
        return s
    return s[0] + " " + s[-1] + (" " + outside_in(s[1:-1]) if len(s) > 2 else "")


def is_palindrome(s: str) -> bool:
    """Recursively determine if a string is a palindrome (ignore case, spaces, punctuation)."""
    # normalise
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    def _pal(x: str) -> bool:
        if len(x) <= 1:
            return True
        if x[0] != x[-1]:
            return False
        return _pal(x[1:-1])
    return _pal(cleaned)


if __name__ == "__main__":
    # Quick self-tests (not formal doctests here to keep it simple in this file)
    assert blocks_loop(6) == 21
    assert blocks_recursive(6) == 21
    assert outside_in("123456") == "1 6 2 5 3 4"
    assert is_palindrome("A Toyota's a Toyota")
    print("Recursion helpers OK")
