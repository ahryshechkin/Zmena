from zmena.application.bridges.bridge import Bridge
from zmena.application.kinds.bridge import BridgeKind
from zmena.domain.semantic_engine.snapshots.fragment import FragmentSnapshot


class FragmentBridge(Bridge):
    def __init__(self):
        super().__init__(BridgeKind.FRAGMENT)

    def translate(self, fragment):
        return FragmentSnapshot(
            tag=fragment.tag,
            name=fragment.name,
            data_type=fragment.data_type,
            nullable=fragment.constraint != "NOT NULL",
        )
