import unittest
from unittest.mock import Mock

from zmena.domain.migration_forge.core.change import Change
from zmena.domain.migration_forge.core.plan import Plan
from zmena.domain.migration_forge.snapshots.state import StateSnapshot
from zmena.domain.migration_forge.statements.add_column import AddColumnStatement
from zmena.domain.migration_forge.statements.alter_data_type import AlterDataTypeStatement
from zmena.domain.migration_forge.statements.drop_column import DropColumnStatement
from zmena.domain.migration_forge.statements.drop_not_null import DropNotNullStatement
from zmena.domain.migration_forge.statements.rename_column import RenameColumnStatement
from zmena.domain.migration_forge.statements.set_not_null import SetNotNullStatement


class TestPlan(unittest.TestCase):
    def test_derive_add_column(self):
        expected = [
            AddColumnStatement(name="col_08", data_type="DATE", nullable=False),
        ]

        state = StateSnapshot(name="col_08", data_type="DATE", nullable=False)
        change = Change(None, state)
        plan = Plan(change)
        actual = plan.derive()

        self.assertCountEqual(expected, actual)

    def test_derive_alter_data_type(self):
        expected = [
            AlterDataTypeStatement(name="col_08", data_type="TIMESTAMP"),
        ]

        before = StateSnapshot(name="col_08", data_type="DATE", nullable=False)
        after = StateSnapshot(name="col_08", data_type="TIMESTAMP", nullable=False)
        change = Change(before, after)
        plan = Plan(change)
        actual = plan.derive()

        self.assertCountEqual(expected, actual)

    def test_derive_drop_column(self):
        expected = [
            DropColumnStatement(name="col_08"),
        ]

        state = StateSnapshot(name="col_08", data_type="DATE", nullable=False)
        change = Change(state, None)
        plan = Plan(change)
        actual = plan.derive()

        self.assertCountEqual(expected, actual)

    def test_derive_drop_not_null(self):
        expected = [
            DropNotNullStatement(name="col_08"),
        ]

        before = StateSnapshot(name="col_08", data_type="DATE", nullable=False)
        after = StateSnapshot(name="col_08", data_type="DATE", nullable=True)
        change = Change(before, after)
        plan = Plan(change)
        actual = plan.derive()

        self.assertCountEqual(expected, actual)

    def test_derive_multiple_changes(self):
        expected = [
            AlterDataTypeStatement(name="col_88", data_type="TIMESTAMP"),
            DropNotNullStatement(name="col_88"),
            RenameColumnStatement(old_name="col_08", new_name="col_88"),
        ]

        before = StateSnapshot(name="col_08", data_type="DATE", nullable=False)
        after = StateSnapshot(name="col_88", data_type="TIMESTAMP", nullable=True)
        change = Change(before, after)
        plan = Plan(change)
        actual = plan.derive()

        self.assertCountEqual(expected, actual)

    def test_derive_rename_column(self):
        expected = [
            RenameColumnStatement(old_name="col_08", new_name="col_88"),
        ]

        before = StateSnapshot(name="col_08", data_type="DATE", nullable=False)
        after = StateSnapshot(name="col_88", data_type="DATE", nullable=False)
        change = Change(before, after)
        plan = Plan(change)
        actual = plan.derive()

        self.assertCountEqual(expected, actual)

    def test_derive_set_not_null(self):
        expected = [
            SetNotNullStatement(name="col_08"),
        ]

        before = StateSnapshot(name="col_08", data_type="DATE", nullable=True)
        after = StateSnapshot(name="col_08", data_type="DATE", nullable=False)
        change = Change(before, after)
        plan = Plan(change)
        actual = plan.derive()

        self.assertCountEqual(expected, actual)

    def test_repr(self):
        plan = Plan(Mock())
        self.assertEqual("Plan", repr(plan))
