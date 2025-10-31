"""
CP1404/CP5632 Practical
Band class (association: Band has Musicians)
Estimate: 15 min
Actual: 12 min
"""


class Band:
    """A simple collection of musicians that can 'play'."""

    def __init__(self, name: str):
        self.name = name
        self.musicians = []  # list of Musician objects

    def __str__(self) -> str:
        # Show the band name and each Musician's string form
        members = ", ".join(str(m) for m in self.musicians)
        return f"{self.name} ({members})"

    def add(self, musician) -> None:
        """Add a Musician to the band."""
        self.musicians.append(musician)

    def play(self) -> str:
        """Return the combined 'play' output for all musicians (each on a new line)."""
        return "\n".join(m.play() for m in self.musicians)
