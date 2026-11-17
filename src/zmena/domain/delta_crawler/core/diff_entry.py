from zmena.domain.delta_crawler.kinds.status import StatusKind


class DiffEntry:
    def __init__(self, entry):
        self.status = StatusKind(entry.split("\t")[0])
        self.pathname = entry.split("\t")[1]

    def __repr__(self):
        return f"DiffEntry(status={self.status})"

    def path(self):
        return self.pathname.replace("\\", "/")

    def has_before(self):
        pass

    def has_after(self):
        pass
