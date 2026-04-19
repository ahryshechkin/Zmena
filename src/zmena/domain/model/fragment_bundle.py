from zmena.domain.types.side import Side


class FragmentBundle:
    def __init__(self, fragments):
        self.fragments = fragments

    def __repr__(self):
        return f"FragmentBundle(fragments={len(self.fragments)})"

    def left(self):
        return [f for f in self.fragments if f.side == Side.LEFT]

    def right(self):
        return [f for f in self.fragments if f.side == Side.RIGHT]
