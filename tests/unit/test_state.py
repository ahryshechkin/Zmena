import unittest

from zmena.domain.migration_forge.snapshots.state import StateSnapshot


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = StateSnapshot(name="col_08", data_type="DATE", nullable=False)

    def test_init(self):
        self.assertEqual("col_08", self.state.name)
        self.assertEqual("DATE", self.state.data_type)
        self.assertFalse(self.state.nullable)

    def test_repr(self):
        self.assertEqual(
            "StateSnapshot(name=col_08,data_type=DATE,nullable=False)", repr(self.state)
        )
