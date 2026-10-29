class ScriptView:
    def __init__(self, sql):
        self.sql = sql

    def __repr__(self):
        return f"ScriptView(sql={len(self.sql)})"

    def details(self):
        return self.sql

    def width(self):
        return len(self.sql)
