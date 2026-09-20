from zmena.application.handoffs.migration_forge.bridges.bridge import Bridge
from zmena.application.handoffs.migration_forge.snapshots.match import MatchSnapshot
from zmena.application.kinds.bridge import BridgeKind


class MatchBundleBridge(Bridge):
    def __init__(self, bridge):
        super().__init__(BridgeKind.MATCH_BUNDLE)
        self.bridge = bridge

    def translate(self, decisions):
        matches = []
        for decision in decisions:
            for winner in decision.winners:
                match = MatchSnapshot(
                    before=self.bridge.translate(winner.left),
                    after=self.bridge.translate(winner.right),
                )
                matches.append(match)

        return matches
