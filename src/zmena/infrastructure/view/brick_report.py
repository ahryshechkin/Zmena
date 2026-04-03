from zmena.infrastructure.view.report import Report


class BrickReport(Report):
    def __init__(self, bricks):
        self.bricks = bricks
        super().__init__(
            [
                ("tag", ">", "8"),
                ("side", ">", "4"),
                ("segment", "<", "8"),
                ("position", ">", "8"),
                ("name", "<", "7"),
                ("type", "<", "13"),
                ("constraint", "<", "10"),
            ]
        )

    def title(self):
        prefix = "#### Bricks "
        width = sum(int(w) + 3 for _, _, w in self.schema) - len(prefix) + 1
        print(f"{prefix}" + "#" * width)

    def body(self):
        for brick in self.bricks:
            print(f"| {brick} |")
