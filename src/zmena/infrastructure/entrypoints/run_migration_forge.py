from zmena.application.bridges.match_bundle import MatchBundleBridge
from zmena.application.bridges.state import StateBridge
from zmena.application.messages.inbound.migration_forge import MigrationForgeInboundMessage
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

    bridge = MatchBundleBridge(StateBridge())
    matches = bridge.translate(seo_message.decisions_new)

    mfi_message = MigrationForgeInboundMessage(matches=matches)
    pipeline = MigrationForgePipeline(mfi_message)
    mfo_message = pipeline.run()
