import unittest

from zmena.domain.migration_forge.core.snapshot import Snapshot


class TestSnapshot(unittest.TestCase):
    def setUp(self):
        self.snapshot = Snapshot(name="col_08", data_type="DATE", nullable=False)

    def test_init_execution(self):
        self.assertEqual("col_08", self.snapshot.name)
        self.assertEqual("DATE", self.snapshot.data_type)
        self.assertFalse(self.snapshot.nullable)

    def test_repr_execution(self):
        self.assertEqual("Snapshot(name=col_08,data_type=DATE,nullable=False)", repr(self.snapshot))
