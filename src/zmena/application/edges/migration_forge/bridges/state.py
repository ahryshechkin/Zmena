from zmena.application.edges.migration_forge.records.state import StateSnapshot


class StateBridge:
    def __repr__(self):
        return "StateBridge(bridges=state)"

    def translate(self, fragment):
        if fragment.tag == "stub":
            return None

        return StateSnapshot(
            name=fragment.name,
            data_type=fragment.data_type,
            nullable=fragment.constraint != "NOT NULL",
        )
