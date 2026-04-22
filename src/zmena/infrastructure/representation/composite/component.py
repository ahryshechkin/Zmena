from zmena.infrastructure.representation.basic.fragment import FragmentReport
from zmena.infrastructure.representation.basic.hypothesis import HypothesisReport
from zmena.infrastructure.representation.composite.composite_report import CompositeReport


class ComponentReport(CompositeReport):
    def __init__(self, components):
        super().__init__("Component")
        self.components = components

    def render(self):
        for i, component in enumerate(self.components, 1):
            title = self.title(
                i, fragments=len(component.fragments), hypotheses=len(component.hypotheses)
            )

            hypothesis_report = HypothesisReport(title, component.hypotheses)
            hypothesis_report.render()

            fragment_report = FragmentReport(title, component.fragments)
            fragment_report.render()
