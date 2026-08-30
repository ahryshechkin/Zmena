from zmena.domain.migration_forge.core.change import Change
from zmena.domain.migration_forge.core.plan import Plan
from zmena.domain.migration_forge.core.snapshot import Snapshot

before = Snapshot(name="col_01", data_type="INT", nullable=True, position=5)
# after = Snapshot(name="col_02", data_type="DATE", nullable=False, position=5)
after = None

change = Change(before, after)
plan = Plan(change)
result = plan.derive()
