from zmena.infrastructure.view.report_simple import ReportSimple


class ReportHypothesis(ReportSimple):
    def __init__(self, hypotheses, desc="Hypotheses"):
        super().__init__(
            desc,
            [
                ("rule", ">", "9"),
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
            hypotheses,
        )
