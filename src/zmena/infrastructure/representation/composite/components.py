from zmena.infrastructure.representation.composite.base import ReportComposite
from zmena.infrastructure.representation.simple.fragment import ReportFragment
from zmena.infrastructure.representation.simple.hypothesis import ReportHypothesis


class ReportComponents(ReportComposite):
    def __init__(self, components):
        super().__init__("Component")
        self.components = components

    def render(self):
        for i, component in enumerate(self.components, 1):
            name = self.compose(
                i, hypotheses=len(component.hypotheses), fragments=len(component.fragments)
            )

            report_hypothesis = ReportHypothesis(component.hypotheses, name)
            report_hypothesis.render()

            report_fragment = ReportFragment(component.fragments, name)
            report_fragment.render()
