from dataclasses import dataclass


@dataclass
class MigrationForgeInboundMessage:
    changes: list

    def __repr__(self):
        return f"MigrationForgeInboundMessage(changes={len(self.changes)})"
