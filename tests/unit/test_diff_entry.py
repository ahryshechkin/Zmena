import unittest

from zmena.domain.delta_crawler.core.diff_entry import DiffEntry


class TestDiffEntry(unittest.TestCase):
    def setUp(self):
        self.entry = DiffEntry("M\tinfra/catalog/sql.py")

    def test_has_after(self):
        self.assertTrue(self.entry.has_after())

    def test_has_before(self):
        self.assertTrue(self.entry.has_before())

    def test_path(self):
        self.assertEqual("infra/catalog/sql.py", self.entry.path())

    def test_repr_execution(self):
        self.assertEqual("DiffEntry(status=M)", repr(self.entry))
