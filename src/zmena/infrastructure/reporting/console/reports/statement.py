from zmena.infrastructure.reporting.console.layouts.basic import BasicReport


class StatementReport(BasicReport):
    def __init__(self, name, statements):
        super().__init__(
            name,
            [
                ("rule", ">", "18"),
                ("####", ">", "4"),
                ("tag", ">", "8"),
                ("block", "<", "8"),
                ("position", ">", "8"),
                ("side", ">", "4"),
                ("name", "<", "7"),
                ("data_type", "<", "13"),
                ("constraint", "<", "10"),
                ("####", ">", "4"),
                ("tag", ">", "8"),
                ("block", "<", "8"),
                ("position", ">", "8"),
                ("side", ">", "4"),
                ("name", "<", "7"),
                ("data_type", "<", "13"),
                ("constraint", "<", "10"),
            ],
            statements,
        )
