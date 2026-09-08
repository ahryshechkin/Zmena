from zmena.application.bridges.match_bundle import MatchBundleBridge
from zmena.application.bridges.state import StateBridge
from zmena.application.messages.inbound.semantic_engine import SemanticEngineInboundMessage
from zmena.application.pipelines.semantic_engine import SemanticEnginePipeline
from zmena.infrastructure.adapters.catalogs.scenario import ScenarioCatalog

sce_ids = ["401"]
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    sei_message = SemanticEngineInboundMessage(
        before=scenario.before.splitlines(), after=scenario.after.splitlines()
    )
    pipeline = SemanticEnginePipeline(sei_message)
    seo_message = pipeline.run()

    bridge = MatchBundleBridge(StateBridge())
    matches = bridge.translate(seo_message.decisions_new)
    # selected_links = [for decision in seo_message.decisions_new]
    # message = MigrationForgeInboundMessage(before=before, after=after)

    # pipeline = MigrationForgePipeline(message)
    # result = pipeline.run()
