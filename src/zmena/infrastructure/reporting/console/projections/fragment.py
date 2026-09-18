from zmena.domain.semantic_engine.kinds.tag import TagKind


class FragmentProjection:
    def __init__(self, fragment):
        self.fragment = fragment

    def caption(self):
        if self.fragment.tag == TagKind.STUB:
            return "Stub"
        return f"{self.fragment.name} ({self.fragment.side}:{self.fragment.position})"
