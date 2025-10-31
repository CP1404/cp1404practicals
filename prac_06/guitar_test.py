"""CP1404/CP5632 Practical 06 – Simple tests for Guitar class.

Estimate: 7 min
Actual: 5min
"""

from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another = Guitar("Another Guitar", 2016, 1000.00)

print(f"{gibson.name} get_age() - Expected 103. Got {gibson.get_age()}")
print(f"{another.name} get_age() - Expected 9. Got {another.get_age()}")

print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")
