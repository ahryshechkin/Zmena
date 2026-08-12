from dataclasses import dataclass


@dataclass(frozen=True)
class SemanticEngineMessage:
    before: str
    after: str

    def __repr__(self):
        return "SemanticEngineMessage"
