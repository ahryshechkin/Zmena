import unittest

from zmena.domain.migration_forge.kinds.statement import StatementKind
from zmena.domain.migration_forge.statements.add_column import AddColumnStatement
from zmena.domain.migration_forge.statements.alter_data_type import AlterDataTypeStatement
from zmena.domain.migration_forge.statements.drop_column import DropColumnStatement
from zmena.domain.migration_forge.statements.drop_not_null import DropNotNullStatement
from zmena.domain.migration_forge.statements.rename_column import RenameColumnStatement
from zmena.domain.migration_forge.statements.set_not_null import SetNotNullStatement
from zmena.domain.migration_forge.statements.statement import Statement


class TestAddColumnStatement(unittest.TestCase):
    def setUp(self):
        self.statement = AddColumnStatement(name="col_08", data_type="DATE", nullable=False)

    def test_init(self):
        self.assertEqual(StatementKind.ADD_COLUMN, self.statement.kind)
        self.assertEqual("col_08", self.statement.name)
        self.assertEqual("DATE", self.statement.data_type)
        self.assertFalse(self.statement.nullable)

    def test_repr(self):
        self.assertEqual(
            "AddColumnStatement(name=col_08,data_type=DATE,nullable=False)", repr(self.statement)
        )


class TestAlterDataTypeStatement(unittest.TestCase):
    def setUp(self):
        self.statement = AlterDataTypeStatement(name="col_08", data_type="TIMESTAMP")

    def test_init(self):
        self.assertEqual(StatementKind.ALTER_DATA_TYPE, self.statement.kind)
        self.assertEqual("col_08", self.statement.name)
        self.assertEqual("TIMESTAMP", self.statement.data_type)

    def test_repr(self):
        self.assertEqual(
            "AlterDataTypeStatement(name=col_08,data_type=TIMESTAMP)",
            repr(self.statement),
        )


class TestDropColumnStatement(unittest.TestCase):
    def setUp(self):
        self.statement = DropColumnStatement(name="col_08")

    def test_init(self):
        self.assertEqual(StatementKind.DROP_COLUMN, self.statement.kind)
        self.assertEqual("col_08", self.statement.name)

    def test_repr(self):
        self.assertEqual("DropColumnStatement(name=col_08)", repr(self.statement))


class TestDropNotNullStatement(unittest.TestCase):
    def setUp(self):
        self.statement = DropNotNullStatement(name="col_08")

    def test_init(self):
        self.assertEqual(StatementKind.DROP_NOT_NULL, self.statement.kind)
        self.assertEqual("col_08", self.statement.name)

    def test_repr(self):
        self.assertEqual("DropNotNullStatement(name=col_08)", repr(self.statement))


class TestRenameColumnStatement(unittest.TestCase):
    def setUp(self):
        self.statement = RenameColumnStatement(old_name="col_08", new_name="col_88")

    def test_init(self):
        self.assertEqual(StatementKind.RENAME_COLUMN, self.statement.kind)
        self.assertEqual("col_08", self.statement.old_name)
        self.assertEqual("col_88", self.statement.new_name)

    def test_repr(self):
        self.assertEqual(
            "RenameColumnStatement(old_name=col_08,new_name=col_88)", repr(self.statement)
        )


class TestSetNotNullStatement(unittest.TestCase):
    def setUp(self):
        self.statement = SetNotNullStatement(name="col_08")

    def test_init(self):
        self.assertEqual(StatementKind.SET_NOT_NULL, self.statement.kind)
        self.assertEqual("col_08", self.statement.name)

    def test_repr(self):
        self.assertEqual("SetNotNullStatement(name=col_08)", repr(self.statement))


class TestStatement(unittest.TestCase):
    def setUp(self):
        self.statement = Statement(kind=StatementKind.UNDEFINED)

    def test_init(self):
        self.assertEqual(StatementKind.UNDEFINED, self.statement.kind)

    def test_repr(self):
        self.assertEqual("Statement(kind=undefined)", repr(self.statement))
