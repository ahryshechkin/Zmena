from zmena.application.handoffs.report_hub.snapshots.component import ComponentSnapshot


class ComponentBridge:
    def __init__(self, fragment_bridge, hypothesis_bridge):
        self.fragment_bridge = fragment_bridge
        self.hypothesis_bridge = hypothesis_bridge

    def translate(self, component):
        fragments = [self.fragment_bridge.translate(fragment) for fragment in component.fragments]
        hypotheses = [
            self.hypothesis_bridge.translate(hypothesis) for hypothesis in component.hypotheses
        ]

        return ComponentSnapshot(fragments=fragments, hypotheses=hypotheses)
