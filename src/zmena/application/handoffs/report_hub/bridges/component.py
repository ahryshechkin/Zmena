from zmena.application.bridges.bridge import Bridge
from zmena.application.handoffs.report_hub.snapshots.component import ComponentSnapshot
from zmena.application.kinds.bridge import BridgeKind


class ComponentBridge(Bridge):
    def __init__(self, fragment_bridge, hypothesis_bridge):
        super().__init__(BridgeKind.COMPONENT)
        self.fragment_bridge = fragment_bridge
        self.hypothesis_bridge = hypothesis_bridge

    def translate(self, component):
        fragments = [self.fragment_bridge.translate(fragment) for fragment in component.fragments]
        hypotheses = [
            self.hypothesis_bridge.translate(hypothesis) for hypothesis in component.hypotheses
        ]

        return ComponentSnapshot(fragments=fragments, hypotheses=hypotheses)
