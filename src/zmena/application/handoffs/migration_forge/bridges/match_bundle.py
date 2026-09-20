from zmena.application.handoffs.migration_forge.snapshots.match import MatchSnapshot


class MatchBundleBridge:
    def __init__(self, bridge):
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
