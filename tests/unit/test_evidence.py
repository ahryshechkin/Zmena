import unittest

from zmena.domain.semantic_engine.core.evidence import Evidence
from zmena.domain.semantic_engine.core.hypothesis import Hypothesis
from zmena.domain.semantic_engine.fragments.left import LeftFragment
from zmena.domain.semantic_engine.fragments.right import RightFragment
from zmena.domain.semantic_engine.types.heuristic_kind import HeuristicKind
from zmena.domain.semantic_engine.types.rule_kind import RuleKind
from zmena.domain.semantic_engine.types.side import Side
from zmena.domain.semantic_engine.types.tag import Tag


class TestEvidence(unittest.TestCase):
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

        hypothesis = Hypothesis(RuleKind.POSITION, left, right)

        self.evidence = Evidence(hypothesis, 1.0, 2.0, HeuristicKind.NAME_SIMILARITY)

    def test_description(self):
        self.assertEqual("2.0  name similarity", self.evidence.description())

    def test_polarity(self):
        self.assertEqual("+", self.evidence.polarity())

    def test_repr(self):
        self.assertEqual(
            "Evidence(signal=1.0,weight=2.0,reason=name similarity)", repr(self.evidence)
        )

    def test_score(self):
        self.assertEqual(2.0, self.evidence.score())
