from zmena.domain.migration_forge.core.snapshot import Snapshot


class SnapshotMint:
    def __repr__(self):
        return "SnapshotMint(mints=snapshot)"

    def issue(self, fragment):
        if fragment.tag == "stub":
            return None

        return Snapshot(
            name=fragment.name,
            data_type=fragment.data_type,
            nullable=fragment.constraint != "NOT NULL",
        )
