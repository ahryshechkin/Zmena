from zmena.application.handoffs.test_suite.records.fragment import FragmentRecord


class FragmentMint:
    def __repr__(self):
        return "FragmentMint(mints=fragment)"

    def issue(self, fragment):
        return FragmentRecord(
            tag=fragment.tag.value,
            block=fragment.block,
            position=fragment.position,
            side=fragment.side.value,
            name=fragment.name,
            data_type=fragment.data_type,
            nullable=fragment.nullable,
        )
