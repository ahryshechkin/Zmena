import unittest
from unittest.mock import Mock

from zmena.domain.semantic_engine.fragments.fragment import Fragment
from zmena.domain.semantic_engine.fragments.left import LeftFragment
from zmena.domain.semantic_engine.fragments.right import RightFragment
from zmena.domain.semantic_engine.fragments.stub import StubFragment
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
        self.hunk = Mock()
        self.hunk.kind.return_value = Tag.REPLACE
        self.hunk.fingerprint.return_value = "03050306"
        self.hunk.left_line.return_value = "col_04 VARCHAR(50) NOT NULL"
        self.hunk.left_lineno.return_value = 4

    def test_init(self):
        fragment = LeftFragment(0, self.hunk)

        self.assertEqual(Tag.REPLACE, fragment.tag)
        self.assertEqual("03050306", fragment.block)
        self.assertEqual(4, fragment.position)
        self.assertEqual(Side.LEFT, fragment.side)
        self.assertEqual("col_04", fragment.name)
        self.assertEqual("VARCHAR(50)", fragment.data_type)
        self.assertEqual("NOT NULL", fragment.constraint)


class TestRightFragment(unittest.TestCase):
    def setUp(self):
        self.hunk = Mock()
        self.hunk.kind.return_value = Tag.REPLACE
        self.hunk.fingerprint.return_value = "03050306"
        self.hunk.right_line.return_value = "col_04 DATE"
        self.hunk.right_lineno.return_value = 4

    def test_init(self):
        fragment = RightFragment(0, self.hunk)

        self.assertEqual(Tag.REPLACE, fragment.tag)
        self.assertEqual("03050306", fragment.block)
        self.assertEqual(4, fragment.position)
        self.assertEqual(Side.RIGHT, fragment.side)
        self.assertEqual("col_04", fragment.name)
        self.assertEqual("DATE", fragment.data_type)
        self.assertIsNone(fragment.constraint)


class TestStubFragment(unittest.TestCase):
    def test_init_left(self):
        fragment = StubFragment(Side.LEFT)

        self.assertEqual(Tag.STUB, fragment.tag)
        self.assertEqual("", fragment.block)
        self.assertEqual("", fragment.position)
        self.assertEqual(Side.LEFT, fragment.side)
        self.assertEqual("", fragment.name)
        self.assertEqual("", fragment.data_type)
        self.assertIsNone(fragment.constraint)

    def test_init_right(self):
        fragment = StubFragment(Side.RIGHT)

        self.assertEqual(Tag.STUB, fragment.tag)
        self.assertEqual("", fragment.block)
        self.assertEqual("", fragment.position)
        self.assertEqual(Side.RIGHT, fragment.side)
        self.assertEqual("", fragment.name)
        self.assertEqual("", fragment.data_type)
        self.assertIsNone(fragment.constraint)
