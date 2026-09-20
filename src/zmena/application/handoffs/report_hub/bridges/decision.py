from zmena.application.handoffs.report_hub.snapshots.decision import DecisionSnapshot


class DecisionBridge:
    def __init__(self, bridge):
        self.bridge = bridge

    def translate(self, decision):
        candidates = [self.bridge.translate(link) for link in decision.candidates()]
        winners = [self.bridge.translate(link) for link in decision.winners()]

        return DecisionSnapshot(candidates=candidates, winners=winners)
