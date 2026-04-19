from zmena.infrastructure.representation.simple.base import ReportSimple


class ReportFragment(ReportSimple):
    def __init__(self, fragments, name="Fragments"):
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
            fragments,
        )
