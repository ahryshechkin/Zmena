import unittest

from zmena.domain.sql_intake.core.sql_table_definition import SQLTableDefinition


class TestSQLTableDefinition(unittest.TestCase):
    def test_all_columns_in_order(self):
        table_definition = SQLTableDefinition("""
        CREATE TABLE t (
            col_01 INT NOT NULL,
            col_02 VARCHAR(50) NOT NULL,
            col_03 VARCHAR(200),
        );
        """)

        self.assertEqual(
            [
                "col_01 INT NOT NULL",
                "col_02 VARCHAR(50) NOT NULL",
                "col_03 VARCHAR(200)",
            ],
            table_definition.normalized_columns(),
        )

    def test_empty_table(self):
        table_definition = SQLTableDefinition("""CREATE TABLE t ();""")
        self.assertEqual(table_definition.normalized_columns(), [])

    def test_one_line_definition(self):
        table_definition = SQLTableDefinition("""
        CREATE TABLE t (col_01 INT NOT NULL, col_02 VARCHAR(50) NOT NULL, col_03 VARCHAR(200));
        """)

        self.assertEqual(
            [
                "col_01 INT NOT NULL",
                "col_02 VARCHAR(50) NOT NULL",
                "col_03 VARCHAR(200)",
            ],
            table_definition.normalized_columns(),
        )

    def test_repr_execution(self):
        table_definition = SQLTableDefinition("""CREATE TABLE t ();""")
        self.assertEqual("SQLTableDefinition(length=18)", repr(table_definition))

    def test_rough_unaligned_definition(self):
        table_definition = SQLTableDefinition("""
        CREATE TABLE t (
            col_01 INT        NOT NULL    ,
                             col_02 VARCHAR             ( 50) not     null,
        col_03 VARCHAR(200)
        );
        """)

        self.assertEqual(
            [
                "col_01 INT NOT NULL",
                "col_02 VARCHAR(50) NOT NULL",
                "col_03 VARCHAR(200)",
            ],
            table_definition.normalized_columns(),
        )

    def test_single_column(self):
        table_definition = SQLTableDefinition("""
        CREATE TABLE t (
            col_01 INT NOT NULL
        );
        """)

        self.assertEqual(["col_01 INT NOT NULL"], table_definition.normalized_columns())
