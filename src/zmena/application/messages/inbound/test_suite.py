from dataclasses import dataclass


@dataclass
class TestSuiteInboundMessage:
    winners: list

    def __repr__(self):
        return f"TestSuiteInboundMessage(winners={len(self.winners)})"
