import unittest

from zmena.domain.migration_forge.core.change import Change
from zmena.domain.migration_forge.core.inference import Inference
from zmena.domain.migration_forge.core.snapshot import Snapshot
from zmena.domain.migration_forge.statements.add_column import AddColumnStatement
from zmena.domain.migration_forge.statements.alter_data_type import AlterDataTypeStatement
from zmena.domain.migration_forge.statements.drop_column import DropColumnStatement
from zmena.domain.migration_forge.statements.drop_not_null import DropNotNullStatement
from zmena.domain.migration_forge.statements.rename_column import RenameColumnStatement
from zmena.domain.migration_forge.statements.set_not_null import SetNotNullStatement


class TestPlan(unittest.TestCase):
    def test_derive_add_column(self):
        expected = [
            AddColumnStatement("tab_01", "col_08", "DATE", nullable=False),
        ]

        snapshot = Snapshot("col_08", "DATE", nullable=False)
        change = Change("tab_01", None, snapshot)
        inference = Inference(change)
        actual = inference.derive()

        self.assertCountEqual(expected, actual)

    def test_derive_alter_data_type(self):
        expected = [
            AlterDataTypeStatement("tab_01", "col_08", "TIMESTAMP"),
        ]

        before = Snapshot("col_08", "DATE", nullable=False)
        after = Snapshot("col_08", "TIMESTAMP", nullable=False)
        change = Change("tab_01", before, after)
        inference = Inference(change)
        actual = inference.derive()

        self.assertCountEqual(expected, actual)

    def test_derive_drop_column(self):
        expected = [
            DropColumnStatement("tab_01", "col_08"),
        ]

        snapshot = Snapshot("col_08", "DATE", nullable=False)
        change = Change("tab_01", snapshot, None)
        inference = Inference(change)
        actual = inference.derive()

        self.assertCountEqual(expected, actual)

    def test_derive_drop_not_null(self):
        expected = [
            DropNotNullStatement("tab_01", "col_08"),
        ]

        before = Snapshot("col_08", "DATE", nullable=False)
        after = Snapshot("col_08", "DATE", nullable=True)
        change = Change("tab_01", before, after)
        inference = Inference(change)
        actual = inference.derive()

        self.assertCountEqual(expected, actual)

    def test_derive_multiple_changes(self):
        expected = [
            AlterDataTypeStatement("tab_01", "col_88", "TIMESTAMP"),
            DropNotNullStatement("tab_01", "col_88"),
            RenameColumnStatement("tab_01", "col_08", "col_88"),
        ]

        before = Snapshot("col_08", "DATE", nullable=False)
        after = Snapshot("col_88", "TIMESTAMP", nullable=True)
        change = Change("tab_01", before, after)
        inference = Inference(change)
        actual = inference.derive()

        self.assertCountEqual(expected, actual)

    def test_derive_rename_column(self):
        expected = [
            RenameColumnStatement("tab_01", "col_08", "col_88"),
        ]

        before = Snapshot("col_08", "DATE", nullable=False)
        after = Snapshot("col_88", "DATE", nullable=False)
        change = Change("tab_01", before, after)
        inference = Inference(change)
        actual = inference.derive()

        self.assertCountEqual(expected, actual)

    def test_derive_set_not_null(self):
        expected = [
            SetNotNullStatement("tab_01", "col_08"),
        ]

        before = Snapshot("col_08", "DATE", nullable=True)
        after = Snapshot("col_08", "DATE", nullable=False)
        change = Change("tab_01", before, after)
        inference = Inference(change)
        actual = inference.derive()

        self.assertCountEqual(expected, actual)

    def test_repr_execution(self):
        snapshot = Snapshot("col_08", "DATE", nullable=False)
        change = Change("tab_01", None, snapshot)
        inference = Inference(change)
        self.assertEqual("Inference(name=tab_01)", repr(inference))
