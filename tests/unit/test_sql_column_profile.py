import unittest
from unittest.mock import Mock

from zmena.domain.sql_intake.core.sql_column_profile import SQLColumnProfile


class TestSQLColumnProfile(unittest.TestCase):
    def setUp(self):
        self.column_def = Mock()
        self.expected = "col_01 INT NOT NULL"

    def test_formatted_sql_lowercase(self):
        self.column_def.sql.return_value = "col_01 int not null"

        profile = SQLColumnProfile(self.column_def)
        actual = profile.formatted_sql()

        self.assertEqual(self.expected, actual)

    def test_formatted_sql_mixed(self):
        self.column_def.sql.return_value = "COL_01 int NoT nuLL"

        profile = SQLColumnProfile(self.column_def)
        actual = profile.formatted_sql()

        self.assertEqual(self.expected, actual)

    def test_formatted_sql_uppercase(self):
        self.column_def.sql.return_value = "COL_01 INT NOT NULL"

        profile = SQLColumnProfile(self.column_def)
        actual = profile.formatted_sql()

        self.assertEqual(self.expected, actual)

    def test_repr(self):
        self.column_def.sql.return_value = self.expected

        profile = SQLColumnProfile(self.column_def)

        self.assertEqual("SQLColumnProfile(definition=col_01 INT NOT NULL)", repr(profile))
