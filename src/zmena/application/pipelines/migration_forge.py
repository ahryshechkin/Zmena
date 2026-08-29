from zmena.domain.migration_forge.core.column_evalution import ColumnEvalution
from zmena.domain.migration_forge.core.migration import Migration
from zmena.domain.migration_forge.core.snapshot import ColumnState

before = ColumnState(name="col_01", data_type="INT", nullable=True, position=5)
after = ColumnState(name="col_02", data_type="INT", nullable=True, position=5)

evaluation = ColumnEvalution()
change = evaluation.between(before, after)
migration = Migration()
result = migration.plan(change)
