import unittest

from zmena.domain.semantic_engine.fragments.fragment import Fragment
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
