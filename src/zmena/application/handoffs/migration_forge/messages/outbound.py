from dataclasses import dataclass


@dataclass
class MigrationForgeOutboundMessage:
    statements: list
    scripts: list

    def __repr__(self):
        return (
            f"MigrationForgeOutboundMessage("
            f"statements={len(self.statements)},scripts={len(self.scripts)}"
            f")"
        )
