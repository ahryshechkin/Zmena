from zmena.application.handoffs.migration_forge.records.state import StateRecord


class StateBridge:
    def __repr__(self):
        return "StateBridge(mints=state)"

    def translate(self, fragment):
        if fragment.tag == "stub":
            return None

        return StateRecord(
            name=fragment.name,
            data_type=fragment.data_type,
            nullable=fragment.constraint != "NOT NULL",
        )
