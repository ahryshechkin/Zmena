from zmena.domain.migration_forge.core.snapshot import Snapshot


class SnapshotMint:
    def __repr__(self):
        return "SnapshotMint(mints=snapshot)"

    def issue(self, fragment):
        if fragment.tag == "stub":
            return None

        return Snapshot(fragment.name, fragment.data_type, fragment.nullable)
