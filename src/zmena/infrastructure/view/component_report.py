from zmena.infrastructure.view.brick_report import BrickReport
from zmena.infrastructure.view.hypothesis_report import HypothesisReport


class ComponentReport:
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

            HypothesisReport(component.hypotheses).render(title)
            BrickReport(component.bricks).render(title)
