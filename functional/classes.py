
class ResistLine:

    resist_lines = []

    def __init__(self, resist_level: float, counter: int) -> None:
        self.level = resist_level
        self.counter = counter
        ResistLine.resist_lines.append(self)

    def __str__(self) -> str:
        return f'Level: {self.level}, Counter: {self.counter}'
