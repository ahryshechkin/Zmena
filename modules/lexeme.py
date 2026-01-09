import re


class Lexeme:
    pattern = r"^(\w+)\s+((\w+)\s*(\(\d+\))?)(\s*(not)?\s+(null)?)?"

    def __init__(self, line):
        self.token = re.search(self.pattern, line, re.IGNORECASE)


    def name(self):
        return self.token.group(1)


    def type(self):
        return self.token.group(2).strip()


    def constraint(self):
        c = self.token.group(5)
        return c.strip() if c else None
