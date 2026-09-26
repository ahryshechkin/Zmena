from zmena.infrastructure.reporting.console.layouts.basic import BasicReport
from zmena.infrastructure.reporting.console.projections.fragment import FragmentProjection
from zmena.infrastructure.reporting.console.projections.hypothesis import HypothesisProjection


class HypothesisReport(BasicReport):
    def __init__(self, name, hypotheses):
        projection = HypothesisProjection(FragmentProjection())
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
            [projection.apply(hypothesis) for hypothesis in hypotheses],
        )
