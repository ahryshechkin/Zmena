from dataclasses import dataclass


@dataclass
class SQLIntakeInboundMessage:
    label: str
    name: str
    before: str
    after: str

    def __repr__(self):
        return f"SQLIntakeInboundMessage(label={self.label},name={self.name})"
