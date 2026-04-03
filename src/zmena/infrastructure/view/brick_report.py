from zmena.infrastructure.view.report import Report


class BrickReport(Report):
    def __init__(self, bricks):
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
        self.bricks = bricks

    def title(self):
        prefix = "\n#### Bricks "
        width = super().title() - len(prefix)
        print(f"{prefix}" + "#" * width)

    def body(self):
        for brick in self.bricks:
            print(f"| {brick} |")
