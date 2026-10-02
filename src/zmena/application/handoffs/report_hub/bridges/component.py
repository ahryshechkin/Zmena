from zmena.application.handoffs.report_hub.records.component import ComponentRecord


class ComponentBridge:
    def __init__(self, fragment_mint, hypothesis_bridge):
        self.fragment_mint = fragment_mint
        self.hypothesis_bridge = hypothesis_bridge

    def __repr__(self):
        return "ComponentBridge(mints=component,hypothesis,fragment)"

    def translate(self, component):
        fragments = [self.fragment_mint.issue(fragment) for fragment in component.fragments]
        hypotheses = [
            self.hypothesis_bridge.translate(hypothesis) for hypothesis in component.hypotheses
        ]

        return ComponentRecord(fragments=fragments, hypotheses=hypotheses)
