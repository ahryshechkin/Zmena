import unittest

from domain import Span


class TestSpan(unittest.TestCase):
    def setUp(self):
        self.before = [
            "col_01 int not null",
            "col_02 varchar(50) not null",
            "col_03 varchar(200)",
            "col_04 varchar(50) not null",
            "col_05 varchar(50)",
            "col_06 int",
            "col_07 varchar(1) not null",
            "col_08 date not null",
            "col_09 datetime2 not null",
            "col_10 datetime2 not null",
        ]

        self.span = Span(self.before, 2, 5)

    def test_uid(self):
        self.assertEqual(self.span.uid(), "25")
