from dataclasses import dataclass


@dataclass
class DeltaCrawlerOutboundMessage:
    cmt_id: str
    name: str
    before: str
    after: str

    def __repr__(self):
        return f"DeltaCrawlerOutboundMessage(cmt_id={self.cmt_id},name={self.name})"
