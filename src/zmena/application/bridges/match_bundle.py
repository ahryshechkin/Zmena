from zmena.application.bridges.bridge import Bridge
from zmena.application.kinds.bridge import BridgeKind
from zmena.domain.migration_forge.snapshots.match import MatchSnapshot


class MatchBundleBridge(Bridge):
    def __init__(self, bridge):
        super().__init__(BridgeKind.MATCH_BUNDLE)
        self.bridge = bridge

    def translate(self, decisions):
        matches = []
        for decision in decisions:
            for selected_link in decision.selected_links:
                match = MatchSnapshot(
                    before=self.bridge.translate(selected_link.left),
                    after=self.bridge.translate(selected_link.right),
                )
                matches.append(match)

        return matches
