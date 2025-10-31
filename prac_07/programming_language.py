"""
CP1404/CP5632 Practical 07 - Programming Language class with an added field.
Estimate: 15 min
Actual: 15 min
"""

class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year, pointer_arithmetic=False):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"Pointer Arithmetic={self.pointer_arithmetic}, First appeared in {self.year}")

    def __repr__(self):
        return str(self)

    def is_dynamic(self):
        return self.typing.lower() == "dynamic"


def run_tests():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    languages = [ruby, python, visual_basic]
    print(python)
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

if __name__ == "__main__":
    run_tests()
