from zmena.application.handoffs.report_hub.bridges.bridge import Bridge
from zmena.application.handoffs.report_hub.snapshots.fragment import FragmentSnapshot
from zmena.application.kinds.bridge import BridgeKind


class FragmentBridge(Bridge):
    def __init__(self):
        super().__init__(BridgeKind.FRAGMENT)

    def translate(self, fragment):
        return FragmentSnapshot(
            tag=fragment.tag.value,
            block=fragment.block,
            position=fragment.position,
            side=fragment.side.value,
            name=fragment.name,
            data_type=fragment.data_type,
            nullable=fragment.constraint != "NOT NULL",
        )
