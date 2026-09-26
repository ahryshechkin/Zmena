from zmena.application.edges.report_hub.handoffs.from_sc import (
    ScenarioCatalogToReportHubHandoff,
)
from zmena.application.edges.sematic_engine.handoffs.from_sc import (
    ScenarioCatalogToSemanticEngineHandoff,
)
from zmena.application.pipelines.semantic_engine import SemanticEnginePipeline
from zmena.infrastructure.adapters.catalogs.scenario import ScenarioCatalog
from zmena.infrastructure.reporting.console.report_hub import ReportHub

sce_ids = ["071"]
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    handoff = ScenarioCatalogToSemanticEngineHandoff(scenario)
    sei_message = handoff.prepare()

    pipeline = SemanticEnginePipeline(sei_message)
    seo_message = pipeline.run()

    handoff = ScenarioCatalogToReportHubHandoff(scenario, seo_message)
    rhi_message = handoff.prepare()

    hub = ReportHub(rhi_message)
    hub.show_sql_diff()
    hub.show_fragments()
    hub.show_hypotheses()
    hub.show_components()
    hub.show_decisions()
