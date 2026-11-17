class DiffEntry:
    def __init__(self, entry):
        self.status = entry.split("\t")[0]
        self.pathname = entry.split("\t")[1]

    def path(self):
        return self.pathname

    def has_before(self):
        pass

    def has_after(self):
        pass
