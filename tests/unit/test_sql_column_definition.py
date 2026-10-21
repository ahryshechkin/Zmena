import unittest
from unittest.mock import Mock

from zmena.domain.sql_intake.core.sql_column_definition import SQLColumnDefinition


class TestSQLColumnDefinition(unittest.TestCase):
    def setUp(self):
        self.column_def = Mock()
        self.expected = "col_01 INT NOT NULL"

    def test_normalized_text_lowercase(self):
        self.column_def.sql.return_value = "col_01 int not null"

        definition = SQLColumnDefinition(self.column_def)
        actual = definition.normalized_text()

        self.assertEqual(self.expected, actual)

    def test_normalized_text_mixed(self):
        self.column_def.sql.return_value = "COL_01 int NoT nuLL"

        definition = SQLColumnDefinition(self.column_def)
        actual = definition.normalized_text()

        self.assertEqual(self.expected, actual)

    def test_normalized_text_uppercase(self):
        self.column_def.sql.return_value = "COL_01 INT NOT NULL"

        definition = SQLColumnDefinition(self.column_def)
        actual = definition.normalized_text()

        self.assertEqual(self.expected, actual)

    def test_repr_execution(self):
        self.column_def.sql.return_value = self.expected

        definition = SQLColumnDefinition(self.column_def)

        self.assertEqual("SQLColumnDefinition(text=col_01 INT NOT NULL)", repr(definition))
