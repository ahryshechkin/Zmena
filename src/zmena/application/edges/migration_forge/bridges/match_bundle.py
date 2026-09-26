from zmena.application.edges.migration_forge.records.match import MatchRecord


class MatchBundleBridge:
    def __init__(self, bridge):
        self.bridge = bridge

    def __repr__(self):
        return "MatchBundleBridge(bridges=state,match_bundle)"

    def translate(self, decisions):
        matches = []
        for decision in decisions:
            for winner in decision.winners():
                match = MatchRecord(
                    before=self.bridge.translate(winner.left),
                    after=self.bridge.translate(winner.right),
                )
                matches.append(match)

        return matches
