from zmena.infrastructure.view.report import Report


class BrickReport(Report):
    def __init__(self):
        super().__init__(
            [
                ("tag", ">", "7"),
                ("side", ">", "4"),
                ("segment", "<", "8"),
                ("position", ">", "8"),
                ("name", "<", "7"),
                ("type", "<", "13"),
                ("constraint", "<", "10"),
            ]
        )
