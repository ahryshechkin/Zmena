from dataclasses import dataclass


@dataclass
class SQLIntakeOutboundMessage:
    name: str
    before: list
    after: list

    def __repr__(self):
        return (
            f"SQLIntakeOutboundMessage("
            f"name={self.name},before={len(self.before)},after={len(self.after)}"
            f")"
        )
