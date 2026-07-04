from zmena.domain.semantic_engine.lenses.lens import Lens
from zmena.domain.semantic_engine.model.evidence import Evidence
from zmena.domain.semantic_engine.types.lens_kind import LensKind


class ColumnSwapLens(Lens):
    def __init__(self):
        super().__init__(LensKind.COLUMN_SWAP)

    def evaluate(self, link, context):
        left, right = link.fragments()
        if not left.same_name_but_different_block_as(right):
            return []

        for first in context.original_links():
            f_left, f_right = first.fragments()
            if left.same_name_as(f_left) and not right.same_name_as(f_right):
                for second in context.original_links():
                    s_left, s_right = second.fragments()
                    if f_left.same_name_as(s_right) and f_right.same_name_as(s_left):
                        return [Evidence("", 1.0, 0.9, self.kind)]

        return []
