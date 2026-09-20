from zmena.application.handoffs.report_hub.semantic_engine_to_report_hub import (
    SemanticEngineToReportHubHandoff,
)
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

    handoff = SemanticEngineToReportHubHandoff(
        kind="SCE", scenario=scenario, seo_message=seo_message
    )
    rhi_message = handoff.prepare()

    hub = ReportHub(rhi_message)
    hub.show_sql_diff()
    hub.show_fragments()
    hub.show_hypotheses()
    hub.show_components()
    hub.show_decisions()
