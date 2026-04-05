from zmena.infrastructure.representation.simple.base import ReportSimple


class ReportLink(ReportSimple):
    def __init__(self, links, name="Links"):
        super().__init__(
            name,
            [
                ("score", ">", "7"),
                ("####", ">", "4"),
                ("tag", ">", "8"),
                ("side", ">", "4"),
                ("segment", "<", "8"),
                ("position", ">", "8"),
                ("name", "<", "7"),
                ("type", "<", "13"),
                ("constraint", "<", "10"),
                ("####", ">", "4"),
                ("tag", ">", "8"),
                ("side", ">", "4"),
                ("segment", "<", "8"),
                ("position", ">", "8"),
                ("name", "<", "7"),
                ("type", "<", "13"),
                ("constraint", "<", "10"),
            ],
            links,
        )
