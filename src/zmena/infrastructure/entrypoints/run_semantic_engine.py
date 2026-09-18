from zmena.application.messages.inbound.report_hub import ReportHubInboundMessage
from zmena.application.messages.inbound.semantic_engine import SemanticEngineInboundMessage
from zmena.application.pipelines.semantic_engine import SemanticEnginePipeline
from zmena.infrastructure.adapters.catalogs.scenario import ScenarioCatalog
from zmena.infrastructure.reporting.console.report_hub import ReportHub

sce_ids = ["071"]
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    sei_message = SemanticEngineInboundMessage(
        before=scenario.before.splitlines(), after=scenario.after.splitlines()
    )
    pipeline = SemanticEnginePipeline(sei_message)
    seo_message = pipeline.run()

    rhi_message = ReportHubInboundMessage(
        kind="SCE",
        label=scenario.sce_id,
        name=scenario.name,
        before=scenario.before.splitlines(),
        after=scenario.after.splitlines(),
        fragments=seo_message.fragments,
        hypotheses=seo_message.hypotheses,
        components=seo_message.components,
        decisions=seo_message.decisions,
    )

    hub = ReportHub(rhi_message)
    hub.show_sql_diff()
    hub.show_fragments()
    hub.show_hypotheses()
    hub.show_components()
    hub.show_decisions()
