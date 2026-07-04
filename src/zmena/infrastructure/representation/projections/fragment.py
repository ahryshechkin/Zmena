from zmena.domain.semantic_engine.types.tag import Tag


class FragmentProjection:
    def __init__(self, fragment):
        self.fragment = fragment

    def caption(self):
        if self.fragment.tag == Tag.STUB:
            return "Stub"
        return f"{self.fragment.name} ({self.fragment.side}:{self.fragment.position})"
