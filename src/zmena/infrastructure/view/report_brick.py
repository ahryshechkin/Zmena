from zmena.infrastructure.view.report_simple import ReportSimple


class ReportBrick(ReportSimple):
    def __init__(self, bricks, desc="Bricks"):
        super().__init__(
            desc,
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
