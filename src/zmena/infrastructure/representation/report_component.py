from zmena.infrastructure.representation.report_brick import ReportBrick
from zmena.infrastructure.representation.report_composite import ReportComposite
from zmena.infrastructure.representation.report_hypothesis import ReportHypothesis


class ReportComponent(ReportComposite):
    def __init__(self, components):
        super().__init__("Component")
        self.components = components

    def render(self):
        for i, component in enumerate(self.components, 1):
            name = self.compose(
                i, hypotheses=len(component.hypotheses), bricks=len(component.bricks)
            )

            report_hypothesis = ReportHypothesis(component.hypotheses, name)
            report_hypothesis.render()

            report_brick = ReportBrick(component.bricks, name)
            report_brick.render()
