from zmena.infrastructure.reporting.console.layouts.basic import BasicReport
from zmena.infrastructure.reporting.console.projections.evidence import EvidenceProjection
from zmena.infrastructure.reporting.console.projections.fragment import FragmentProjection
from zmena.infrastructure.reporting.console.projections.link import LinkProjection


class LinkReport(BasicReport):
    def __init__(self, name, links):
        projection = LinkProjection(FragmentProjection(), EvidenceProjection())
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
            [projection.apply(link) for link in links],
        )
