from zmena.application.handoffs.migration_forge.snapshots.state import StateSnapshot
from zmena.application.handoffs.report_hub.bridges.bridge import Bridge
from zmena.application.kinds.bridge import BridgeKind


class StateBridge(Bridge):
    def __init__(self):
        super().__init__(BridgeKind.STATE)

    def translate(self, fragment):
        if fragment.tag == "stub":
            return None

        return StateSnapshot(
            name=fragment.name, data_type=fragment.data_type, nullable=fragment.nullable
        )
