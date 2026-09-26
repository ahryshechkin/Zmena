from dataclasses import dataclass


@dataclass
class MigrationForgeOutboundMessage:
    statements: list

    def __repr__(self):
        return f"MigrationForgeOutboundMessage(statements={len(self.statements)})"
