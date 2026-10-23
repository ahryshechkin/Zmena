import unittest

from zmena.domain.migration_forge.core.change import Change
from zmena.domain.migration_forge.core.snapshot import Snapshot


class TestChange(unittest.TestCase):
    def setUp(self):
        self.before = Snapshot("col_08", "DATE", nullable=False)
        self.after = Snapshot("col_88", "TIMESTAMP", nullable=True)
        self.change = Change("tab_01", self.before, self.after)

    def test_has_data_type_change(self):
        self.assertTrue(self.change.has_data_type_change())

    def test_has_data_type_change_when_after_is_none(self):
        change = Change("tab_01", self.before, None)
        self.assertFalse(change.has_data_type_change())

    def test_has_name_change(self):
        self.assertTrue(self.change.has_name_change())

    def test_has_name_change_when_after_is_none(self):
        change = Change("tab_01", self.before, None)
        self.assertFalse(change.has_name_change())

    def test_has_nullability_change(self):
        self.assertTrue(self.change.has_nullability_change())

    def test_has_nullability_change_when_after_is_none(self):
        change = Change("tab_01", self.before, None)
        self.assertFalse(change.has_nullability_change())

    def test_is_add(self):
        self.assertFalse(self.change.is_add())

    def test_is_drop(self):
        self.assertFalse(self.change.is_drop())

    def test_name(self):
        self.assertEqual("tab_01", self.change.name())

    def test_repr_execution(self):
        self.assertEqual("Change(before=True,after=True)", repr(self.change))

    def test_snapshots(self):
        self.assertEqual((self.before, self.after), self.change.snapshots())
