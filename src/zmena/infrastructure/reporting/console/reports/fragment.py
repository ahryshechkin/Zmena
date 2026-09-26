from zmena.infrastructure.reporting.console.layouts.basic import BasicReport
from zmena.infrastructure.reporting.console.projections.fragment import FragmentProjection


class FragmentReport(BasicReport):
    def __init__(self, name, fragments):
        projection = FragmentProjection()
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
            [projection.apply(fragment) for fragment in fragments],
        )
