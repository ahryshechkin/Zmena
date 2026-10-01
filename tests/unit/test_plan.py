import unittest
from unittest.mock import Mock

from zmena.application.handoffs.migration_forge.records.state import StateRecord
from zmena.domain.migration_forge.core.change import Change
from zmena.domain.migration_forge.core.plan import Plan
from zmena.domain.migration_forge.statements.add_column import AddColumnStatement
from zmena.domain.migration_forge.statements.alter_data_type import AlterDataTypeStatement
from zmena.domain.migration_forge.statements.drop_column import DropColumnStatement
from zmena.domain.migration_forge.statements.drop_not_null import DropNotNullStatement
from zmena.domain.migration_forge.statements.rename_column import RenameColumnStatement
from zmena.domain.migration_forge.statements.set_not_null import SetNotNullStatement


class TestPlan(unittest.TestCase):
    def test_derive_add_column(self):
        expected = [
            AddColumnStatement("col_08", "DATE", nullable=False),
        ]

        state = StateRecord(name="col_08", data_type="DATE", nullable=False)
        change = Change(None, state)
        plan = Plan(change)
        actual = plan.derive()

        self.assertCountEqual(expected, actual)

    def test_derive_alter_data_type(self):
        expected = [
            AlterDataTypeStatement("col_08", "TIMESTAMP"),
        ]

        before = StateRecord(name="col_08", data_type="DATE", nullable=False)
        after = StateRecord(name="col_08", data_type="TIMESTAMP", nullable=False)
        change = Change(before, after)
        plan = Plan(change)
        actual = plan.derive()

        self.assertCountEqual(expected, actual)

    def test_derive_drop_column(self):
        expected = [
            DropColumnStatement("col_08"),
        ]

        state = StateRecord(name="col_08", data_type="DATE", nullable=False)
        change = Change(state, None)
        plan = Plan(change)
        actual = plan.derive()

        self.assertCountEqual(expected, actual)

    def test_derive_drop_not_null(self):
        expected = [
            DropNotNullStatement("col_08"),
        ]

        before = StateRecord(name="col_08", data_type="DATE", nullable=False)
        after = StateRecord(name="col_08", data_type="DATE", nullable=True)
        change = Change(before, after)
        plan = Plan(change)
        actual = plan.derive()

        self.assertCountEqual(expected, actual)

    def test_derive_multiple_changes(self):
        expected = [
            AlterDataTypeStatement("col_88", "TIMESTAMP"),
            DropNotNullStatement("col_88"),
            RenameColumnStatement("col_08", "col_88"),
        ]

        before = StateRecord(name="col_08", data_type="DATE", nullable=False)
        after = StateRecord(name="col_88", data_type="TIMESTAMP", nullable=True)
        change = Change(before, after)
        plan = Plan(change)
        actual = plan.derive()

        self.assertCountEqual(expected, actual)

    def test_derive_rename_column(self):
        expected = [
            RenameColumnStatement("col_08", "col_88"),
        ]

        before = StateRecord(name="col_08", data_type="DATE", nullable=False)
        after = StateRecord(name="col_88", data_type="DATE", nullable=False)
        change = Change(before, after)
        plan = Plan(change)
        actual = plan.derive()

        self.assertCountEqual(expected, actual)

    def test_derive_set_not_null(self):
        expected = [
            SetNotNullStatement("col_08"),
        ]

        before = StateRecord(name="col_08", data_type="DATE", nullable=True)
        after = StateRecord(name="col_08", data_type="DATE", nullable=False)
        change = Change(before, after)
        plan = Plan(change)
        actual = plan.derive()

        self.assertCountEqual(expected, actual)

    def test_repr_execution(self):
        plan = Plan(Mock())
        self.assertEqual("Plan", repr(plan))
