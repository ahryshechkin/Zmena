import unittest

from zmena.domain.migration_forge.core.change import Change
from zmena.domain.migration_forge.snapshots.state import Snapshot


class TestChange(unittest.TestCase):
    def setUp(self):
        self.before = Snapshot(name="col_08", data_type="DATE", nullable=False)
        self.after = Snapshot(name="col_88", data_type="TIMESTAMP", nullable=True)
        self.change = Change(self.before, self.after)

    def test_has_data_type_change(self):
        self.assertTrue(self.change.has_data_type_change())

    def test_has_data_type_change_when_after_is_none(self):
        change = Change(self.before, None)
        self.assertFalse(change.has_data_type_change())

    def test_has_name_change(self):
        self.assertTrue(self.change.has_name_change())

    def test_has_name_change_when_after_is_none(self):
        change = Change(self.before, None)
        self.assertFalse(change.has_name_change())

    def test_has_nullability_change(self):
        self.assertTrue(self.change.has_nullability_change())

    def test_has_nullability_change_when_after_is_none(self):
        change = Change(self.before, None)
        self.assertFalse(change.has_nullability_change())

    def test_is_add(self):
        self.assertFalse(self.change.is_add())

    def test_is_drop(self):
        self.assertFalse(self.change.is_drop())

    def test_repr(self):
        self.assertEqual("Change(before=True,after=True)", repr(self.change))

    def test_snapshots(self):
        self.assertEqual((self.before, self.after), self.change.snapshots())
