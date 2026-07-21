import unittest
from unittest.mock import Mock

from zmena.domain.semantic_engine.core.evidence import Evidence
from zmena.domain.semantic_engine.core.link import Link
from zmena.domain.semantic_engine.fragments.left import LeftFragment
from zmena.domain.semantic_engine.fragments.right import RightFragment
from zmena.domain.semantic_engine.types.heuristic_kind import HeuristicKind
from zmena.domain.semantic_engine.types.side import Side
from zmena.domain.semantic_engine.types.tag import Tag


class TestLink(unittest.TestCase):
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

        self.link = Link(self.left, self.right)
        self.other = Link(self.left, self.right)

        self.evidence_ns = Evidence(Mock(), 1.0, 2.0, HeuristicKind.NAME_SIMILARITY)
        self.evidence_ps = Evidence(Mock(), 1.0, 0.6, HeuristicKind.POSITION_SIMILARITY)

    def test_add_evidence(self):
        self.link.add_evidence(self.evidence_ns)
        self.link.add_evidence(self.evidence_ps)
        self.assertCountEqual([self.evidence_ns, self.evidence_ps], self.link.evidences)

    def test_fragments(self):
        self.assertEqual((self.left, self.right), self.link.fragments())

    def test_lt(self):
        self.link.add_evidence(self.evidence_ns)
        self.link.add_evidence(self.evidence_ps)
        self.other.add_evidence(self.evidence_ns)

        self.assertTrue(self.link > self.other)

    def test_repr(self):
        self.link.add_evidence(self.evidence_ns)
        self.link.add_evidence(self.evidence_ps)
        self.assertEqual("Link(score=2.6,evidences=2)", repr(self.link))

    def test_score(self):
        self.assertEqual(0.0, self.link.score())

    def test_str(self):
        self.link.add_evidence(self.evidence_ns)
        self.assertEqual(
            "    2.0 | "
            "#### |  replace | 03050306 |        4 |    L | col_04  | VARCHAR(50)   |   NOT NULL | "
            "#### |  replace | 03050306 |        4 |    R | col_04  | DATE          |           ",
            str(self.link),
        )
