import unittest

from zmena.domain.sql_intake.sql_column_profile import SQLColumnProfile


class TestSQLColumnProfile(unittest.TestCase):
    def test_all_columns_in_order(self):
        sql_column_profile = SQLColumnProfile("""
        CREATE TABLE t (
            col_01 INT NOT NULL,
            col_02 VARCHAR(50) NOT NULL,
            col_03 VARCHAR(200),
        );
        """)

        self.assertEqual(
            [
                "COL_01 INT NOT NULL",
                "COL_02 VARCHAR(50) NOT NULL",
                "COL_03 VARCHAR(200)",
            ],
            sql_column_profile.snapshot(),
        )

    def test_empty_table(self):
        sql_column_profile = SQLColumnProfile("""CREATE TABLE t ();""")
        self.assertEqual(sql_column_profile.snapshot(), [])

    def test_one_line_definition(self):
        sql_column_profile = SQLColumnProfile("""
        CREATE TABLE t (col_01 INT NOT NULL, col_02 VARCHAR(50) NOT NULL, col_03 VARCHAR(200));
        """)

        self.assertEqual(
            [
                "COL_01 INT NOT NULL",
                "COL_02 VARCHAR(50) NOT NULL",
                "COL_03 VARCHAR(200)",
            ],
            sql_column_profile.snapshot(),
        )

    def test_rough_unaligned_definition(self):
        sql_column_profile = SQLColumnProfile("""
        CREATE TABLE t (
            col_01 INT        NOT NULL    ,
                             col_02 VARCHAR             ( 50) not     null,
        col_03 VARCHAR(200)
        );
        """)

        self.assertEqual(
            [
                "COL_01 INT NOT NULL",
                "COL_02 VARCHAR(50) NOT NULL",
                "COL_03 VARCHAR(200)",
            ],
            sql_column_profile.snapshot(),
        )

    def test_single_column(self):
        sql_column_profile = SQLColumnProfile("""
        CREATE TABLE t (
            col_01 INT NOT NULL
        );
        """)

        self.assertEqual(["COL_01 INT NOT NULL"], sql_column_profile.snapshot())
