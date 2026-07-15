import unittest

from zmena.domain.semantic_engine.core.hunk import Hunk
from zmena.domain.semantic_engine.core.span import Span
from zmena.domain.semantic_engine.fragments.fragment import Fragment
from zmena.domain.semantic_engine.fragments.left import LeftFragment
from zmena.domain.semantic_engine.types.side import Side
from zmena.domain.semantic_engine.types.tag import Tag


class TestFragment(unittest.TestCase):
    def setUp(self):
        self.fragment = Fragment(
            Tag.REPLACE, "03050306", 4, Side.LEFT, "col_04", "VARCHAR(50)", "NOT NULL"
        )

        self.other = Fragment(Tag.REPLACE, "03050306", 5, Side.LEFT, "col_05", "VARCHAR(50)", None)

    def test_is_delete(self):
        self.assertFalse(self.fragment.is_delete())

    def test_is_insert(self):
        self.assertFalse(self.fragment.is_insert())

    def test_is_replace(self):
        self.assertTrue(self.fragment.is_replace())

    def test_repr(self):
        self.assertEqual("Fragment(tag=replace,name=col_04)", repr(self.fragment))

    def test_same_name_as(self):
        self.assertFalse(self.fragment.same_name_as(self.other))

    def test_same_name_but_different_block_as(self):
        self.assertFalse(self.fragment.same_name_but_different_block_as(self.other))

    def test_same_position_as(self):
        self.assertFalse(self.fragment.same_position_as(self.other))

    def test_same_signature_as(self):
        self.assertFalse(self.fragment.same_signature_as(self.other))

    def test_str(self):
        self.assertEqual(
            " replace | 03050306 |        4 |    L | col_04  | VARCHAR(50)   |   NOT NULL",
            str(self.fragment),
        )


class TestLeftFragment(unittest.TestCase):
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

    def test_init(self):
        fragment = LeftFragment(0, self.hunk)

        self.assertEqual(Tag.REPLACE, fragment.tag)
        self.assertEqual("03050306", fragment.block)
        self.assertEqual(4, fragment.position)
        self.assertEqual(Side.LEFT, fragment.side)
        self.assertEqual("col_04", fragment.name)
        self.assertEqual("VARCHAR(50)", fragment.data_type)
        self.assertEqual("NOT NULL", fragment.constraint)
