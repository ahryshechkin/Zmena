import unittest

from zmena.domain.sql_intake.sql_table_profile import SQLTableProfile


class TestSQLColumnProfile(unittest.TestCase):
    def test_all_columns_in_order(self):
        sql_table_profile = SQLTableProfile("""
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
            sql_table_profile.formatted_columns(),
        )

    def test_empty_table(self):
        sql_table_profile = SQLTableProfile("""CREATE TABLE t ();""")
        self.assertEqual(sql_table_profile.formatted_columns(), [])

    def test_one_line_definition(self):
        sql_table_profile = SQLTableProfile("""
        CREATE TABLE t (col_01 INT NOT NULL, col_02 VARCHAR(50) NOT NULL, col_03 VARCHAR(200));
        """)

        self.assertEqual(
            [
                "col_01 INT NOT NULL",
                "col_02 VARCHAR(50) NOT NULL",
                "col_03 VARCHAR(200)",
            ],
            sql_table_profile.formatted_columns(),
        )

    def test_rough_unaligned_definition(self):
        sql_table_profile = SQLTableProfile("""
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
            sql_table_profile.formatted_columns(),
        )

    def test_single_column(self):
        sql_table_profile = SQLTableProfile("""
        CREATE TABLE t (
            col_01 INT NOT NULL
        );
        """)

        self.assertEqual(["col_01 INT NOT NULL"], sql_table_profile.formatted_columns())
