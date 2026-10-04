from zmena.infrastructure.reporting.console.views.fragment import FragmentView


class FragmentMint:
    def __repr__(self):
        return "FragmentMint(mints=fragment)"

    def issue(self, fragment):
        return FragmentView(
            fragment.tag.value,
            fragment.block,
            fragment.position,
            fragment.side.value,
            fragment.name,
            fragment.data_type,
            "" if fragment.nullable else "NOT NULL",
        )
