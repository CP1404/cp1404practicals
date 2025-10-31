"""CP1404/CP5632 Practical 06 – ProgrammingLanguage class.

Estimate: 10 min
Actual: 10min
"""


class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name: str, typing: str, reflection: bool, year: int) -> None:
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self) -> bool:
        return self.typing.lower() == "dynamic"

    def __str__(self) -> str:
        return (f"{self.name}, {self.typing} Typing, "
                f"Reflection={self.reflection}, First appeared in {self.year}")
