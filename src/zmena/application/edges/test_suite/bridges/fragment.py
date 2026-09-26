from zmena.application.edges.report_hub.records.fragment import FragmentSnapshot


class FragmentBridge:
    def __repr__(self):
        return "FragmentBridge(bridges=fragment)"

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
