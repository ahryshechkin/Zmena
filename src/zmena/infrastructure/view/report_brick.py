from zmena.infrastructure.view.report_simple import ReportSimple


class ReportBrick(ReportSimple):
    def __init__(self, bricks, name="Bricks"):
        super().__init__(
            name,
            [
                ("tag", ">", "8"),
                ("side", ">", "4"),
                ("segment", "<", "8"),
                ("position", ">", "8"),
                ("name", "<", "7"),
                ("type", "<", "13"),
                ("constraint", "<", "10"),
            ],
            bricks,
        )
