import unittest
from unittest.mock import Mock

from zmena.domain.semantic_engine.core.evidence import Evidence
from zmena.domain.semantic_engine.types.heuristic_kind import HeuristicKind


class TestEvidence(unittest.TestCase):
    def setUp(self):
        self.evidence = Evidence(Mock(), 1.0, 2.0, HeuristicKind.NAME_SIMILARITY)

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
