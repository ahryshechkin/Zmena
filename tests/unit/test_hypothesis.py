import unittest

from zmena.domain.semantic_engine.core.hypothesis import Hypothesis
from zmena.domain.semantic_engine.fragments.left import LeftFragment
from zmena.domain.semantic_engine.fragments.right import RightFragment
from zmena.domain.semantic_engine.types.rule_kind import RuleKind
from zmena.domain.semantic_engine.types.side import Side
from zmena.domain.semantic_engine.types.tag import Tag


class TestHypothesis(unittest.TestCase):
    def setUp(self):
        self.left = object.__new__(LeftFragment)
        self.left.tag = Tag.REPLACE
        self.left.block = "03050306"
        self.left.position = 4
        self.left.side = Side.LEFT
        self.left.name = "col_04"
        self.left.data_type = "VARCHAR(50)"
        self.left.constraint = "NOT NULL"

        self.right = object.__new__(RightFragment)
        self.right.tag = Tag.REPLACE
        self.right.block = "03050306"
        self.right.position = 4
        self.right.side = Side.RIGHT
        self.right.name = "col_04"
        self.right.data_type = "DATE"
        self.right.constraint = None

        self.hypothesis = Hypothesis(RuleKind.POSITION, self.left, self.right)

    def test_has_block_mismatch(self):
        self.assertFalse(self.hypothesis.has_block_mismatch())

    def test_has_same_name(self):
        self.assertTrue(self.hypothesis.has_same_name())

    def test_has_same_position(self):
        self.assertTrue(self.hypothesis.has_same_position())

    def test_has_same_signature(self):
        self.assertFalse(self.hypothesis.has_same_signature())

    def test_key(self):
        self.assertEqual((self.left, self.right), self.hypothesis.key())

    def test_neighbor_left(self):
        self.assertEqual(self.left, self.hypothesis.neighbor(self.right))

    def test_neighbor_right(self):
        self.assertEqual(self.right, self.hypothesis.neighbor(self.left))

    def test_repr(self):
        self.assertEqual("Hypothesis(rule=position)", repr(self.hypothesis))

    def test_str(self):
        self.assertEqual(
            "          position | "
            "#### |  replace | 03050306 |        4 |    L | col_04  | VARCHAR(50)   |   NOT NULL | "
            "#### |  replace | 03050306 |        4 |    R | col_04  | DATE          |           ",
            str(self.hypothesis),
        )
