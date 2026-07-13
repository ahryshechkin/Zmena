import unittest

from zmena.domain.semantic_engine.core.hunk import Hunk
from zmena.domain.semantic_engine.core.span import Span
from zmena.domain.semantic_engine.types.tag import Tag


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
            "col_08 DATE NOT NULL",
            "col_09 DATETIME2 NOT NULL",
            "col_10 DATETIME2 NOT NULL",
        ]

        self.after = [
            "col_01 INT NOT NULL",
            "col_02 VARCHAR(50) NOT NULL",
            "col_03 VARCHAR(200)",
            "col_04 DATE",
            "col_05 DATE NOT NULL",
            "col_07 VARCHAR(1) NOT NULL",
            "col_06 INT",
            "col_08 DATE NOT NULL",
            "col_09 DATETIME2 NOT NULL",
            "col_10 DATETIME2 NOT NULL",
        ]

        self.left = Span(self.before, 3, 5)
        self.right = Span(self.after, 3, 6)
        self.hunk = Hunk(Tag.REPLACE, self.left, self.right)

    def test_fingerprint(self):
        self.assertEqual("03050306", self.hunk.fingerprint())

    def test_height(self):
        self.assertEqual(3, self.hunk.height())

    def test_kind(self):
        self.assertEqual(Tag.REPLACE, self.hunk.kind())

    def test_left_line_in_range(self):
        self.assertEqual(self.before[3], self.hunk.left_line(0))

    def test_left_line_out_of_range(self):
        self.assertEqual("", self.hunk.left_line(2))

    def test_left_lineno_in_range(self):
        self.assertEqual(4, self.hunk.left_lineno(0))

    def test_left_lineno_out_of_range(self):
        self.assertEqual("", self.hunk.left_lineno(2))

    def test_left_range(self):
        self.assertEqual(2, self.hunk.left_range())

    def test_repr(self):
        self.assertEqual("Hunk(tag=replace)", repr(self.hunk))

    def test_right_line_in_range(self):
        self.assertEqual(self.after[5], self.hunk.right_line(2))

    def test_right_line_out_of_range(self):
        self.assertEqual("", self.hunk.right_line(3))

    def test_right_lineno_in_range(self):
        self.assertEqual(6, self.hunk.right_lineno(2))

    def test_right_lineno_out_of_range(self):
        self.assertEqual("", self.hunk.right_lineno(3))

    def test_right_range(self):
        self.assertEqual(3, self.hunk.right_range())
