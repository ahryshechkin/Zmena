from zmena.application.handoffs.report_hub.scenario_catalog import ScenarioCatalogToReportHubHandoff
from zmena.application.handoffs.sematic_engine.sql_intake import SQLIntakeToSemanticEngineHandoff
from zmena.application.handoffs.sql_intake.scenario_catalog import ScenarioCatalogToSQLIntakeHandoff
from zmena.application.pipelines.semantic_engine import SemanticEnginePipeline
from zmena.application.pipelines.sql_intake import SQLIntakePipeline
from zmena.infrastructure.adapters.catalogs.scenario import ScenarioCatalog
from zmena.infrastructure.reporting.console.report_hub import ReportHub

sce_ids = ["701"]
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    handoff = ScenarioCatalogToSQLIntakeHandoff(scenario)
    sii_message = handoff.prepare()

    pipeline = SQLIntakePipeline(sii_message)
    sio_message = pipeline.run()

    handoff = SQLIntakeToSemanticEngineHandoff(sio_message)
    sei_message = handoff.prepare()

    pipeline = SemanticEnginePipeline(sei_message)
    seo_message = pipeline.run()

    handoff = ScenarioCatalogToReportHubHandoff(scenario, seo_message)
    rhi_message = handoff.prepare()

    report = ReportHub(rhi_message)
    report.show_sql_diff()
    report.show_fragments()
    report.show_hypotheses()
    report.show_components()
    report.show_decisions()
