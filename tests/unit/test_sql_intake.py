import unittest

from zmena.infrastructure.adapters.sql_intake import SQLIntake


class TestSQLIntake(unittest.TestCase):
    def test_all_columns_in_order(self):
        sql_intake = SQLIntake("""
        CREATE TABLE t (
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(200),
        );
        """)

        self.assertEqual(
            sql_intake.columns(),
            [
                "col_01 int not null",
                "col_02 varchar(50) not null",
                "col_03 varchar(200)",
            ],
        )

    def test_empty_table(self):
        sql_intake = SQLIntake("""CREATE TABLE t ();""")
        self.assertEqual(sql_intake.columns(), [])

    def test_single_column(self):
        sql_intake = SQLIntake("""
        CREATE TABLE t (
            col_01 int not null
        );
        """)

        self.assertEqual(sql_intake.columns(), ["col_01 int not null"])

    def test_rough_unaligned_definition(self):
        sql_intake = SQLIntake("""
        CREATE TABLE t (
            col_01 int        not null    ,
                             col_02 varchar             ( 50) not     null,
        col_03 varchar(200)
        );
        """)

        self.assertEqual(
            sql_intake.columns(),
            [
                "col_01 int not null",
                "col_02 varchar(50) not null",
                "col_03 varchar(200)",
            ],
        )

    def test_one_line_definition(self):
        sql_intake = SQLIntake("""
        CREATE TABLE t (col_01 int not null, col_02 varchar(50) not null, col_03 varchar(200));
        """)

        self.assertEqual(
            sql_intake.columns(),
            [
                "col_01 int not null",
                "col_02 varchar(50) not null",
                "col_03 varchar(200)",
            ],
        )
