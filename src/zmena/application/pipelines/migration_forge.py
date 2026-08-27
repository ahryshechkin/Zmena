from zmena.domain.migration_forge.core.column_evalution import ColumnEvalution
from zmena.domain.migration_forge.core.column_state import ColumnState

before = ColumnState(name="col_01", data_type="INT", nullable=True, position=5)
after = ColumnState(name="col_01", data_type="INT", nullable=False, position=5)

evaluation = ColumnEvalution()
column_change = evaluation.between(before, after)
