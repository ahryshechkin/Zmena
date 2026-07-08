from zmena.domain.semantic_engine.fragments.fragment import Fragment
from zmena.domain.semantic_engine.types.tag import Tag


class StubFragment(Fragment):
    def __init__(self, side):
        super().__init__(Tag.STUB, "", "", side, "", "", None)
