
class ResistLine:

    resist_lines = []

    def __init__(self, resist_level: float, counter: int) -> None:
        self.level = resist_level
        self.counter = counter
        if self.contains(resist_level):
            self.update_lines(resist_level, counter)
        else:
            ResistLine.resist_lines.append(self)

    def __str__(self) -> str:
        return f'Level: {self.level}, Counter: {self.counter}'

    def contains(self, resist_level):
        for line in self.resist_lines:
            if line.level == resist_level:
                return True
        return False

    def update_lines(self, resist_level: float, counter: int) -> None:
        for line in self.resist_lines:
            if line.level == resist_level:
                line.counter = counter

