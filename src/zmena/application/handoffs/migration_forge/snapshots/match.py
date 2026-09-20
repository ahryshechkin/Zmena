from dataclasses import dataclass

from zmena.application.handoffs.migration_forge.snapshots.state import StateSnapshot  # noqa: TC001


@dataclass
class MatchSnapshot:
    before: StateSnapshot | None
    after: StateSnapshot | None

    def __repr__(self):
        return f"MatchSnapshot(before={self.before is not None},after={self.after is not None})"
