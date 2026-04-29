from zmena.domain.model.fragments.fragment import Fragment
from zmena.domain.types.tag import Tag


class StubFragment(Fragment):
    def __init__(self, side):
        super().__init__(Tag.STUB, side, "", "", "", "", None)
