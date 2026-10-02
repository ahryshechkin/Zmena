from zmena.infrastructure.reporting.console.views.fragment import FragmentView


class FragmentMint:
    def __repr__(self):
        return "FragmentMint(mint=fragment)"

    def issue(self, fragment):
        return FragmentView(
            tag=fragment.tag.value,
            block=fragment.block,
            position=fragment.position,
            side=fragment.side.value,
            name=fragment.name,
            data_type=fragment.data_type,
            nullable=fragment.constraint or "",
        )
