from zmena.application.handoffs.report_hub.snapshots.fragment import FragmentSnapshot


class FragmentBridge:
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
