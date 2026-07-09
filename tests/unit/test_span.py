import unittest

from zmena.domain.semantic_engine.core.span import Span


class TestSpan(unittest.TestCase):
    def setUp(self):
        self.before = [
            "col_01 int not null",
            "col_02 varchar(50) not null",
            "col_03 varchar(200)",
            "col_04 varchar(50) not null",
            "col_05 varchar(50)",
            "col_06 int",
            "col_07 varchar(1) not null",
            "col_08 date not null",
            "col_09 datetime2 not null",
            "col_10 datetime2 not null",
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
