from dataclasses import dataclass

from zmena.application.edges.migration_forge.records.state import StateSnapshot  # noqa: TC001


@dataclass
class MatchSnapshot:
    before: StateSnapshot | None
    after: StateSnapshot | None

    def __repr__(self):
        return f"MatchSnapshot(before={self.before is not None},after={self.after is not None})"
