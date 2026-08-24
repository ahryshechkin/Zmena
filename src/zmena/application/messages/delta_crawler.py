from dataclasses import dataclass


@dataclass(frozen=True)
class DeltaCrawlerMessage:
    commit_from: str
    commit_to: str

    def __repr__(self):
        return f"SemanticEngineMessage(commit_from={self.commit_from},commit_to={self.commit_to})"
