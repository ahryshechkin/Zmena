from zmena.application.handoffs.report_hub.semantic_engine_to_report_hub import ReportHubHandoff
from zmena.application.messages.inbound.semantic_engine import SemanticEngineInboundMessage
from zmena.application.messages.inbound.sql_intake import SQLIntakeInboundMessage
from zmena.application.pipelines.semantic_engine import SemanticEnginePipeline
from zmena.application.pipelines.sql_intake import SQLIntakePipeline
from zmena.infrastructure.adapters.catalogs.scenario import ScenarioCatalog
from zmena.infrastructure.reporting.console.report_hub import ReportHub

sce_ids = ["701"]
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    sii_message = SQLIntakeInboundMessage(
        label=scenario.sce_id, name=scenario.name, before=scenario.before, after=scenario.after
    )
    pipeline = SQLIntakePipeline(sii_message)
    sio_message = pipeline.run()

    sei_message = SemanticEngineInboundMessage(before=sio_message.before, after=sio_message.after)
    pipeline = SemanticEnginePipeline(sei_message)
    seo_message = pipeline.run()

    handoff = ReportHubHandoff("SCE", scenario, seo_message)
    rhi_message = handoff.prepare()

    report = ReportHub(rhi_message)
    report.show_sql_diff()
    # report.show_fragments()
    # report.show_hypotheses()
    # report.show_components()
    # report.show_decisions()
