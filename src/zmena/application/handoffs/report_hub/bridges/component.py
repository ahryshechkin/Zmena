from zmena.application.handoffs.report_hub.records.component import ComponentRecord


class ComponentBridge:
    def __init__(self, fragment_mint, hypothesis_mint):
        self.fragment_mint = fragment_mint
        self.hypothesis_mint = hypothesis_mint

    def __repr__(self):
        return "ComponentBridge(mints=component,hypothesis,fragment)"

    def translate(self, component):
        fragments = [self.fragment_mint.issue(fragment) for fragment in component.fragments]
        hypotheses = [self.hypothesis_mint.issue(hypothesis) for hypothesis in component.hypotheses]

        return ComponentRecord(fragments=fragments, hypotheses=hypotheses)
