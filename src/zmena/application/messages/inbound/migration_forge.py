from dataclasses import dataclass


@dataclass
class MigrationForgeInboundMessage:
    matches: list

    def __repr__(self):
        return f"MigrationForgeInboundMessage(matches={len(self.matches)})"
