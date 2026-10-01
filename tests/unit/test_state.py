import unittest

from zmena.application.handoffs.migration_forge.records.state import StateRecord


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = StateRecord(name="col_08", data_type="DATE", nullable=False)

    def test_init_execution(self):
        self.assertEqual("col_08", self.state.name)
        self.assertEqual("DATE", self.state.data_type)
        self.assertFalse(self.state.nullable)

    def test_repr_execution(self):
        self.assertEqual("StateRecord(name=col_08,data_type=DATE,nullable=False)", repr(self.state))
