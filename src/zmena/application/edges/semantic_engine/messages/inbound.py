from dataclasses import dataclass


@dataclass
class SemanticEngineInboundMessage:
    before: str
    after: str

    def __repr__(self):
        return f"SemanticEngineInboundMessage(before={len(self.before)},after={len(self.after)})"
