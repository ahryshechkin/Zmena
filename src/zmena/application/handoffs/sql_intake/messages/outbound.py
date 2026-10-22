from dataclasses import dataclass


@dataclass
class SQLIntakeOutboundMessage:
    tab_name: str
    before: list
    after: list

    def __repr__(self):
        return (
            f"SQLIntakeOutboundMessage("
            f"tab_name={self.tab_name},before={len(self.before)},after={len(self.after)}"
            f")"
        )
