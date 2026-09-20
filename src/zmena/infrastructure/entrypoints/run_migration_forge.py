from zmena.application.handoffs.migration_forge.semantic_engine import (
    SemanticEngineToMigrationForgeHandoff,
)
from zmena.application.messages.inbound.semantic_engine import SemanticEngineInboundMessage
from zmena.application.pipelines.migration_forge import MigrationForgePipeline
from zmena.application.pipelines.semantic_engine import SemanticEnginePipeline
from zmena.infrastructure.adapters.catalogs.scenario import ScenarioCatalog

sce_ids = ["011"]
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    sei_message = SemanticEngineInboundMessage(
        before=scenario.before.splitlines(), after=scenario.after.splitlines()
    )
    pipeline = SemanticEnginePipeline(sei_message)
    seo_message = pipeline.run()

    handoff = SemanticEngineToMigrationForgeHandoff(seo_message)
    mfi_message = handoff.prepare()

    pipeline = MigrationForgePipeline(mfi_message)
    mfo_message = pipeline.run()
