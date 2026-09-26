from dataclasses import dataclass

from zmena.application.edges.migration_forge.records.state import StateRecord  # noqa: TC001


@dataclass
class MatchRecord:
    before: StateRecord | None
    after: StateRecord | None

    def __repr__(self):
        return f"MatchRecord(before={self.before is not None},after={self.after is not None})"
