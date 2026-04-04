from zmena.infrastructure.view.report import Report


class ReportLink(Report):
    def __init__(self, links):
        super().__init__(
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
            ]
        )
        self.links = links

    def title(self, alias=None):
        prefix = alias or "\n#### Links "
        width = self.length() - len(prefix)
        print(f"{prefix}" + "#" * width)

    def body(self):
        for link in self.links:
            print(f"| {link} |")
