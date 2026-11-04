from dataclasses import dataclass


@dataclass
class ReleaseVaultInboundMessage:
    tab_name: str
    sql_text: str

    def __repr__(self):
        return f"ReleaseVaultInboundMessage(tab_name={self.tab_name})"
