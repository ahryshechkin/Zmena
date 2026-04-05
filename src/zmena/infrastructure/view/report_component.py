from zmena.infrastructure.view.report_brick import ReportBrick
from zmena.infrastructure.view.report_composite import ReportComposite
from zmena.infrastructure.view.report_hypothesis import ReportHypothesis


class ReportComponent(ReportComposite):
    def __init__(self, components):
        self.components = components

    def body(self):
        for i, component in enumerate(self.components, 1):
            desc = self.title(
                "Component", i, hypotheses=len(component.hypotheses), bricks=len(component.bricks)
            )

            report_hypothesis = ReportHypothesis(component.hypotheses, desc)
            report_hypothesis.render()

            report_brick = ReportBrick(component.bricks, desc)
            report_brick.render()
