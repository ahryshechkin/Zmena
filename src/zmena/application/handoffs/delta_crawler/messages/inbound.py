from dataclasses import dataclass

from zmena.infrastructure.adapters.commands.git import GitCommand  # noqa: TC001


@dataclass
class DeltaCrawlerInboundMessage:
    command: GitCommand
    commit_from: str
    commit_to: str

    def __repr__(self):
        return (
            f"DeltaCrawlerInboundMessage(commit_from={self.commit_from},commit_to={self.commit_to})"
        )
