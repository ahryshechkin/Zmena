from zmena.domain.semantic_engine.snapshots.fragment import FragmentSnapshot


class FragmentProjection:
    def from_domain(self, fragment):
        return FragmentSnapshot(
            name=fragment.name,
            data_type=fragment.data_type,
            nullability=fragment.constraint != "NOT NULL",
        )
