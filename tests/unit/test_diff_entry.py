import unittest

from zmena.domain.delta_crawler.core.diff_entry import DiffEntry


class TestDiffEntry(unittest.TestCase):
    def setUp(self):
        self.entry = DiffEntry("M\tinfra/catalog/sql.py")

    def test_repr_execution(self):
        self.assertEqual("DiffEntry(status=M)", repr(self.entry))
