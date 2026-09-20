from zmena.application.handoffs.migration_forge.snapshots.state import StateSnapshot


class StateBridge:
    def translate(self, fragment):
        if fragment.tag == "stub":
            return None

        return StateSnapshot(
            name=fragment.name, data_type=fragment.data_type, nullable=fragment.nullable
        )
