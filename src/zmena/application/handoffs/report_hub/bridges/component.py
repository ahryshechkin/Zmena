from zmena.application.handoffs.report_hub.records.component import ComponentRecord


class ComponentBridge:
    def __init__(self, fragment_bridge, hypothesis_bridge):
        self.fragment_bridge = fragment_bridge
        self.hypothesis_bridge = hypothesis_bridge

    def __repr__(self):
        return "ComponentBridge(bridges=component,hypothesis,fragment)"

    def translate(self, component):
        fragments = [self.fragment_bridge.translate(fragment) for fragment in component.fragments]
        hypotheses = [
            self.hypothesis_bridge.translate(hypothesis) for hypothesis in component.hypotheses
        ]

        return ComponentRecord(fragments=fragments, hypotheses=hypotheses)
