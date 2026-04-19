from zmena.domain.types.tag import Tag

from .fragment import Fragment


class StubFragment(Fragment):
    def __init__(self, side):
        super().__init__(Tag.STUB, side, "", "", "", "", None)
