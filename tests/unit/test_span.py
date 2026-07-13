import unittest

from zmena.domain.semantic_engine.core.span import Span


class TestSpan(unittest.TestCase):
    def setUp(self):
        self.before = [
            "col_01 INT NOT NULL",
            "col_02 VARCHAR(50) NOT NULL",
            "col_03 VARCHAR(200)",
            "col_04 VARCHAR(50) NOT NULL",
            "col_05 VARCHAR(50)",
            "col_06 INT",
            "col_07 VARCHAR(1) NOT NULL",
            "col_08 DATE NOT NULL",
            "col_09 DATETIME2 NOT NULL",
            "col_10 DATETIME2 NOT NULL",
        ]

        self.span = Span(self.before, 2, 5)

    def test_fingerprint(self):
        self.assertEqual("0205", self.span.fingerprint())

    def test_line(self):
        self.assertEqual(self.before[2], self.span.line(0))

    def test_lineno(self):
        self.assertEqual(2, self.span.lineno(0))

    def test_range(self):
        self.assertEqual(3, self.span.range())

    def test_repr(self):
        self.assertEqual("Span(lines=10,low=2,high=5)", repr(self.span))
