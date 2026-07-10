import re


class ColumnSpec:
    PATTERN = re.compile(
        r"^(?P<name>\w+)\s+"
        r"(?P<data_type>\w+(?:\(\d+\))?)"
        r"(?:\s+(?P<constraint>not\s+null|null))?$",
        re.IGNORECASE,
    )

    def __init__(self, line):
        self.match = self.PATTERN.search(line)

    def __repr__(self):
        return "ColumnSpec"

    def name(self):
        return self.match.group("name")

    def data_type(self):
        return self.match.group("data_type")

    def constraint(self):
        c = self.match.group("constraint")
        return " ".join(c.split()) if c else None
