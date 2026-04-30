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

    def left_by_block(self):
        fragments = {}
        for fragment in self.left():
            fragments.setdefault(fragment.block, []).append(fragment)

        return fragments

    def right_by_block(self):
        fragments = {}
        for fragment in self.right():
            fragments.setdefault(fragment.block, []).append(fragment)

        return fragments
