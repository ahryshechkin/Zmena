from zmena.domain.semantic_engine.kinds.projection import ProjectionKind
from zmena.domain.semantic_engine.projections.projection import Projection
from zmena.domain.semantic_engine.snapshots.fragment import FragmentSnapshot


class FragmentProjection(Projection):
    def __init__(self):
        super().__init__(ProjectionKind.FRAGMENT)

    def from_domain(self, fragment):
        return FragmentSnapshot(
            tag=fragment.tag,
            name=fragment.name,
            data_type=fragment.data_type,
            nullable=fragment.constraint != "NOT NULL",
        )
