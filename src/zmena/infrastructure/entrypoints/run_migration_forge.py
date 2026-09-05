from zmena.application.messages.inbound.migration_forge import MigrationForgeInboundMessage
from zmena.application.messages.inbound.semantic_engine import SemanticEngineInboundMessage
from zmena.application.pipelines.migration_forge import MigrationForgePipeline
from zmena.application.pipelines.semantic_engine import SemanticEnginePipeline
from zmena.domain.migration_forge.core.snapshot import Snapshot
from zmena.infrastructure.adapters.catalogs.scenario_catalog import ScenarioCatalog

sce_ids = ["011"]
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    sei_message = SemanticEngineInboundMessage(
        before=scenario.before.splitlines(), after=scenario.after.splitlines()
    )
    pipeline = SemanticEnginePipeline(sei_message)
    seo_message = pipeline.run()

    left, right = seo_message.decisions[0].winners()[0].fragments()
    before = None
    after = Snapshot(
        name=right.name, data_type=right.data_type, nullable=right.constraint != "NOT NULL"
    )
    message = MigrationForgeInboundMessage(before=before, after=after)

    pipeline = MigrationForgePipeline(message)
    result = pipeline.run()
    print(result)
