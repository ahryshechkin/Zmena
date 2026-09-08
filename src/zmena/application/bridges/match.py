from zmena.application.bridges.bridge import Bridge
from zmena.application.kinds.bridge import BridgeKind
from zmena.domain.migration_forge.snapshots.match import MatchSnapshot


class MatchBridge(Bridge):
    def __init__(self, bridge):
        super().__init__(BridgeKind.MATCH)
        self.bridge = bridge

    def translate(self, decision):
        matches = []
        for selected_link in decision.selected_links:
            match = MatchSnapshot(
                before=self.bridge.translate(selected_link.left),
                after=self.bridge.translate(selected_link.right),
            )
            matches.append(match)

        return matches
