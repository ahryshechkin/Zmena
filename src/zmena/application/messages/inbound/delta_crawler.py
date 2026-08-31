from dataclasses import dataclass


@dataclass
class DeltaCrawlerInboundMessage:
    commit_from: str
    commit_to: str

    def __repr__(self):
        return (
            f"DeltaCrawlerInboundMessage(commit_from={self.commit_from},commit_to={self.commit_to})"
        )
