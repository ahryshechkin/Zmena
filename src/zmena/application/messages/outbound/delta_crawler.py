from dataclasses import dataclass


@dataclass
class DeltaCrawlerOutboundMessage:
    label: str
    name: str
    before: str
    after: str

    def __repr__(self):
        return f"DeltaCrawlerOutboundMessage(label={self.label},name={self.name})"
