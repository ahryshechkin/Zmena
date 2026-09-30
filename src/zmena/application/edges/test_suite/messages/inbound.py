from dataclasses import dataclass


@dataclass
class TestSuiteInboundMessage:
    links: list
    statements: list

    def __repr__(self):
        return f"TestSuiteInboundMessage(links={len(self.links)},statements={len(self.statements)})"
