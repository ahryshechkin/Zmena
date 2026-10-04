from zmena.application.handoffs.test_suite.records.fragment import FragmentRecord


class FragmentMint:
    def __repr__(self):
        return "FragmentMint(mints=fragment)"

    def issue(self, fragment):
        return FragmentRecord(
            fragment.tag.value,
            fragment.block,
            fragment.position,
            fragment.side.value,
            fragment.name,
            fragment.data_type,
            fragment.nullable,
        )
