from zmena.application.handoffs.migration_forge.semantic_engine import (
    SemanticEngineToMigrationForgeHandoff,
)
from zmena.application.handoffs.sematic_engine.scenario_catalog import (
    ScenarioCatalogToSemanticEngineHandoff,
)
from zmena.application.pipelines.migration_forge import MigrationForgePipeline
from zmena.application.pipelines.semantic_engine import SemanticEnginePipeline
from zmena.infrastructure.adapters.catalogs.scenario import ScenarioCatalog

sce_ids = ["011"]
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    handoff = ScenarioCatalogToSemanticEngineHandoff(scenario)
    sei_message = handoff.prepare()

    pipeline = SemanticEnginePipeline(sei_message)
    seo_message = pipeline.run()

    handoff = SemanticEngineToMigrationForgeHandoff(seo_message)
    mfi_message = handoff.prepare()

    pipeline = MigrationForgePipeline(mfi_message)
    mfo_message = pipeline.run()
