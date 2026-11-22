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

        sieve = PathSieve(self.entries)
        actual = sieve.filter()

        self.assertCountEqual(
            [entry.path() for entry in expected], [entry.path() for entry in actual]
        )

    def test_filter_empty_entries(self):
        expected = []

        sieve = PathSieve([])
        actual = sieve.filter()

        self.assertCountEqual(expected, actual)

    def test_filter_without_matches(self):
        expected = []

        entries = [
            DiffEntry(entry)
            for entry in [
                "M\tcode/scripts/script.py",
                "M\ttext.txt",
            ]
        ]
        sieve = PathSieve(entries)
        actual = sieve.filter()

        self.assertCountEqual(expected, actual)

    def test_repr_execution(self):
        sieve = PathSieve(self.entries)
        self.assertEqual("PathSieve(entries=13)", repr(sieve))
