import unittest

from zmena.domain.semantic_engine.core.hunk import Hunk
from zmena.domain.semantic_engine.core.span import Span


class TestHunk(unittest.TestCase):
    def setUp(self):
        self.before = [
            "col_01 INT NOT NULL",
            "col_02 VARCHAR(50) NOT NULL",
            "col_03 VARCHAR(200)",
            "col_04 VARCHAR(50) NOT NULL",
            "col_05 VARCHAR(50)",
            "col_06 INT",
            "col_07 VARCHAR(1) NOT NULL",
            "col_08 date NOT NULL",
            "col_09 datetime2 NOT NULL",
            "col_10 datetime2 NOT NULL",
        ]

        self.before = [
            "col_01 INT NOT NULL",
            "col_02 VARCHAR(50) NOT NULL",
            "col_03 VARCHAR(200)",
            "col_04 DATE",
            "col_05 DATE NOT NULL",
            "col_07 VARCHAR(1) NOT NULL",
            "col_06 INT",
            "col_08 date NOT NULL",
            "col_09 datetime2 NOT NULL",
            "col_10 datetime2 NOT NULL",
        ]

        self.span = Span(self.before, 3, 5)
        self.span = Span(self.before, 3, 6)
        self.hunk = Hunk

    def test_repr(self):
        pass

    def test_kind(self):
        pass

    def test_fingerprint(self):
        pass

    def test_left_line(self):
        pass

    def test_left_lineno(self):
        pass

    def test_left_range(self):
        pass

    def test_right_line(self):
        pass

    def test_right_lineno(self):
        pass

    def test_right_range(self):
        pass

    def test_height(self):
        pass
