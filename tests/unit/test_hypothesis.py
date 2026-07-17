import unittest

from zmena.domain.semantic_engine.core.hypothesis import Hypothesis
from zmena.domain.semantic_engine.fragments.left import LeftFragment
from zmena.domain.semantic_engine.fragments.right import RightFragment
from zmena.domain.semantic_engine.types.rule_kind import RuleKind
from zmena.domain.semantic_engine.types.side import Side
from zmena.domain.semantic_engine.types.tag import Tag


class TestHypothesis(unittest.TestCase):
    def setUp(self):
        left = object.__new__(LeftFragment)
        left.tag = Tag.REPLACE
        left.block = "03050306"
        left.position = 4
        left.side = Side.LEFT
        left.name = "col_04"
        left.data_type = "VARCHAR(50)"
        left.constraint = "NOT NULL"

        right = object.__new__(RightFragment)
        right.tag = Tag.REPLACE
        right.block = "03050306"
        right.position = 4
        right.side = Side.RIGHT
        right.name = "col_04"
        right.data_type = "DATE"
        right.constraint = None

        self.hypothesis = Hypothesis(RuleKind.POSITION, left, right)

    def test_has_block_mismatch(self):
        pass

    def test_has_same_name(self):
        pass

    def test_has_same_position(self):
        pass

    def test_has_same_signature(self):
        pass

    def test_key(self):
        pass

    def test_neighbor(self):
        pass

    def test_repr(self):
        pass

    def test_str(self):
        pass
