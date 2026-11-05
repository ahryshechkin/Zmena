from dataclasses import dataclass
from pathlib import Path  # noqa: TC003


@dataclass
class ReleaseVaultInboundMessage:
    target_location: Path
    tab_name: str
    migration: str

    def __repr__(self):
        return f"ReleaseVaultInboundMessage(tab_name={self.tab_name})"
