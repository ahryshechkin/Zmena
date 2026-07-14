import unittest

from zmena.domain.semantic_engine.core.column_spec import ColumnSpec


class TestColumnSpec(unittest.TestCase):
    def test_constraint_absence(self):
        column_spec = ColumnSpec("col_03 VARCHAR(200)")
        self.assertIsNone(column_spec.constraint())

    def test_constraint_not_null(self):
        column_spec = ColumnSpec("col_01 INT NOT NULL")
        self.assertEqual("NOT NULL", column_spec.constraint())

    def test_constraint_null(self):
        column_spec = ColumnSpec("col_01 INT NULL")
        self.assertEqual("NULL", column_spec.constraint())

    def test_data_type(self):
        column_spec = ColumnSpec("col_01 INT NOT NULL")
        self.assertEqual("INT", column_spec.data_type())

    def test_extra_whitespaces(self):
        column_spec = ColumnSpec("col_01    INT    NOT    NULL")
        self.assertEqual("col_01", column_spec.name())
        self.assertEqual("INT", column_spec.data_type())
        self.assertEqual("NOT NULL", column_spec.constraint())

    def test_name(self):
        column_spec = ColumnSpec("col_01 INT NOT NULL")
        self.assertEqual("col_01", column_spec.name())

    def test_repr(self):
        column_spec = ColumnSpec("col_01 INT NOT NULL")
        self.assertEqual("ColumnSpec", repr(column_spec))
