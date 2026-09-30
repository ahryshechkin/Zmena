from dataclasses import dataclass


@dataclass
class TestSuiteInboundMessage:
    winners: list
    statements: list

    def __repr__(self):
        return (
            f"TestSuiteInboundMessage("
            f"winners={len(self.winners)},statements={len(self.statements)}"
            f")"
        )
