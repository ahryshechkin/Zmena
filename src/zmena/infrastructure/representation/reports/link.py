from zmena.infrastructure.representation.layouts.basic import BasicReport


class LinkReport(BasicReport):
    def __init__(self, name, links):
        super().__init__(
            name,
            [
                ("score", ">", "7"),
                ("####", ">", "4"),
                ("tag", ">", "8"),
                ("block", "<", "8"),
                ("position", ">", "8"),
                ("side", ">", "4"),
                ("name", "<", "7"),
                ("type", "<", "13"),
                ("constraint", "<", "10"),
                ("####", ">", "4"),
                ("tag", ">", "8"),
                ("block", "<", "8"),
                ("position", ">", "8"),
                ("side", ">", "4"),
                ("name", "<", "7"),
                ("type", "<", "13"),
                ("constraint", "<", "10"),
            ],
            links,
        )
