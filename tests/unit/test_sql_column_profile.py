import unittest

from zmena.domain.sql_intake.sql_column_profile import SQLColumnProfile


class TestSQLColumnProfile(unittest.TestCase):
    def test_all_columns_in_order(self):
        sql_column_profile = SQLColumnProfile("""
        CREATE TABLE t (
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(200),
        );
        """)

        self.assertEqual(
            sql_column_profile.snapshot(),
            [
                "col_01 int not null",
                "col_02 varchar(50) not null",
                "col_03 varchar(200)",
            ],
        )

    def test_empty_table(self):
        sql_column_profile = SQLColumnProfile("""CREATE TABLE t ();""")
        self.assertEqual(sql_column_profile.snapshot(), [])

    def test_one_line_definition(self):
        sql_column_profile = SQLColumnProfile("""
        CREATE TABLE t (col_01 int not null, col_02 varchar(50) not null, col_03 varchar(200));
        """)

        self.assertEqual(
            sql_column_profile.snapshot(),
            [
                "col_01 int not null",
                "col_02 varchar(50) not null",
                "col_03 varchar(200)",
            ],
        )

    def test_rough_unaligned_definition(self):
        sql_column_profile = SQLColumnProfile("""
        CREATE TABLE t (
            col_01 int        not null    ,
                             col_02 varchar             ( 50) not     null,
        col_03 varchar(200)
        );
        """)

        self.assertEqual(
            sql_column_profile.snapshot(),
            [
                "col_01 int not null",
                "col_02 varchar(50) not null",
                "col_03 varchar(200)",
            ],
        )

    def test_single_column(self):
        sql_column_profile = SQLColumnProfile("""
        CREATE TABLE t (
            col_01 int not null
        );
        """)

        self.assertEqual(sql_column_profile.snapshot(), ["col_01 int not null"])
