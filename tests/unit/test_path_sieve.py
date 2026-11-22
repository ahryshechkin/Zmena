import unittest

from zmena.domain.delta_crawler.core.diff_entry import DiffEntry
from zmena.domain.delta_crawler.core.path_sieve import PathSieve


class TestPathSieve(unittest.TestCase):
    def setUp(self):
        self.entries = [
            DiffEntry(entry)
            for entry in [
                "M\tcode/scripts/script.py",
                "M\tcode/scripts/script.y",
                "M\tcode/scripts/sql.sql",
                "M\tcode/scripts/sql.txt",
                "M\tcode/sql/scripts/script.py",
                "M\tinfra/catalog/schema/tab.sql",
                "M\tinfra/catalog/sql.py",
                "M\tinfra/catalog/sql/script.py",
                "M\tinfra/catalog/sql/tab.sql",
                "M\tinfra\\catalog\\schema\\script.sql",
                "M\tsql.sql",
                "M\ttext.sql",
                "M\ttext.txt",
            ]
        ]
        self.sieve = PathSieve(self.entries)

    def test_filter(self):
        expected = [
            DiffEntry(entry)
            for entry in [
                "M\tcode/scripts/sql.sql",
                "M\tinfra/catalog/schema/tab.sql",
                "M\tinfra/catalog/sql/tab.sql",
                "M\tinfra\\catalog\\schema\\script.sql",
                "M\tsql.sql",
                "M\ttext.sql",
            ]
        ]
        actual = self.sieve.filter()

        self.assertCountEqual(
            [entry.path() for entry in expected], [entry.path() for entry in actual]
        )
