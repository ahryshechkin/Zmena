class FragmentView:
    def __init__(self, fragment):
        self.fragment = fragment

    def __str__(self):
        nullable = "" if self.fragment.nullable else "NOT NULL"
        return (
            f"{self.fragment.tag:>8} | {self.fragment.block:>8} | "
            f"{self.fragment.position:>8} | {self.fragment.side:>4} | "
            f"{self.fragment.name:<7} | {self.fragment.data_type:<13} | {nullable:>10}"
        )

    def caption(self):
        if self.fragment.tag == "stub":
            return "Stub"
        return f"{self.fragment.name} ({self.fragment.side}:{self.fragment.position})"
