from zmena.infrastructure.view.report_brick import ReportBrick
from zmena.infrastructure.view.report_hypothesis import ReportHypothesis


class ReportComponent:
    def __init__(self, components):
        self.components = components

    def render(self):
        self.body()

    def body(self):
        for i, component in enumerate(self.components, 1):
            title = (
                f"\n#### Component {i}: "
                f"hypotheses={len(component.hypotheses)}, bricks={len(component.bricks)} "
            )

            ReportHypothesis(component.hypotheses).render(title)
            ReportBrick(component.bricks).render(title)
