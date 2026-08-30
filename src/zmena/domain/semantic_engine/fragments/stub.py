from zmena.domain.semantic_engine.fragments.fragment import Fragment
from zmena.domain.semantic_engine.kinds.tag import TagKind


class StubFragment(Fragment):
    def __init__(self, side):
        super().__init__(TagKind.STUB, "", "", side, "", "", None)
