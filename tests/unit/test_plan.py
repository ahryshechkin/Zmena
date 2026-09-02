import unittest

from zmena.domain.migration_forge.core.change import Change
from zmena.domain.migration_forge.core.plan import Plan
from zmena.domain.migration_forge.core.snapshot import Snapshot
from zmena.domain.migration_forge.statements.add_column import AddColumnStatement
from zmena.domain.migration_forge.statements.drop_column import DropColumnStatement


class TestPlan(unittest.TestCase):
    def test_derive_add(self):
        expected = [
            AddColumnStatement(name="col_08", data_type="DATE", nullable=False),
        ]

        snapshot = Snapshot(name="col_08", data_type="DATE", nullable=False)
        change = Change(None, snapshot)
        plan = Plan(change)
        actual = plan.derive()

        self.assertCountEqual(expected, actual)

    def test_derive_drop(self):
        expected = [
            DropColumnStatement(name="col_08"),
        ]

        snapshot = Snapshot(name="col_08", data_type="DATE", nullable=False)
        change = Change(snapshot, None)
        plan = Plan(change)
        actual = plan.derive()

        self.assertCountEqual(expected, actual)
