from zmena.infrastructure.view.report import Report


class ReportHypothesis(Report):
    def __init__(self, hypotheses):
        super().__init__(
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
            ]
        )
        self.hypotheses = hypotheses

    def title(self, alias=None):
        prefix = alias or "\n#### Hypotheses "
        width = self.length() - len(prefix)
        print(f"{prefix}" + "#" * width)

    def body(self):
        for hypothesis in self.hypotheses:
            print(f"| {hypothesis} |")
