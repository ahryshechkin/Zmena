from dataclasses import dataclass


@dataclass
class SQLIntakeOutboundMessage:
    before: list
    after: list

    def __repr__(self):
        return f"SQLIntakeOutboundMessage(before={len(self.before)},after={len(self.after)})"
