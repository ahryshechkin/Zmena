from zmena.infrastructure.reporting.console.layouts.composite import CompositeReport
from zmena.infrastructure.reporting.console.reports.fragment import FragmentReport
from zmena.infrastructure.reporting.console.reports.hypothesis import HypothesisReport


class ComponentReport(CompositeReport):
    def __init__(self, components):
        super().__init__("Component")
        self.components = components

    def render(self):
        for i, component in enumerate(self.components, 1):
            title = self.title(i, hypotheses=len(component.hypotheses))
            hypothesis_report = HypothesisReport(title, component.hypotheses)
            hypothesis_report.render()

            title = self.title(i, fragments=len(component.fragments))
            fragment_report = FragmentReport(title, component.fragments)
            fragment_report.render()
