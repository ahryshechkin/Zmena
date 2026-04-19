from zmena.infrastructure.representation.basic.basic_report import BasicReport


class FragmentReport(BasicReport):
    def __init__(self, name, fragments):
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
