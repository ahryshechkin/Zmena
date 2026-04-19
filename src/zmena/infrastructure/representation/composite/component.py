from zmena.infrastructure.representation.composite.base import ReportComposite
from zmena.infrastructure.representation.simple.fragment import FragmentReport
from zmena.infrastructure.representation.simple.hypothesis import HypothesisReport


class ComponentReport(ReportComposite):
    def __init__(self, components):
        super().__init__("Component")
        self.components = components

    def render(self):
        for i, component in enumerate(self.components, 1):
            name = self.compose(
                i, hypotheses=len(component.hypotheses), fragments=len(component.fragments)
            )

            hypothesis_report = HypothesisReport(name, component.hypotheses)
            hypothesis_report.render()

            fragment_report = FragmentReport(name, component.fragments)
            fragment_report.render()
