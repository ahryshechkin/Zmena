from zmena.application.messages.migration_forge import MigrationForgeMessage
from zmena.application.pipelines.migration_forge import MigrationForgePipeline
from zmena.domain.migration_forge.core.snapshot import Snapshot

message = MigrationForgeMessage(
    before=Snapshot(name="col_01", data_type="INT", nullable=True),
    after=Snapshot(name="col_02", data_type="DATE", nullable=False),
)
pipeline = MigrationForgePipeline(message)
result = pipeline.run()
