from zmena.infrastructure.representation.layouts.basic import BasicReport


class FragmentReport(BasicReport):
    def __init__(self, name, fragments):
        super().__init__(
            name,
            [
                ("tag", ">", "8"),
                ("block", "<", "8"),
                ("position", ">", "8"),
                ("side", ">", "4"),
                ("name", "<", "7"),
                ("data_type", "<", "13"),
                ("constraint", "<", "10"),
            ],
            fragments,
        )
