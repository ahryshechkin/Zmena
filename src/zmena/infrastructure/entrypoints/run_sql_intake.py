from zmena.application.messages.analysis_report import AnalysisReportMessage
from zmena.application.messages.inbound.sql_intake import SQLIntakeInboundMessage
from zmena.application.pipelines.semantic_engine import SemanticEnginePipeline
from zmena.application.pipelines.sql_intake import SQLIntakePipeline
from zmena.infrastructure.adapters.scenario_catalog import ScenarioCatalog
from zmena.infrastructure.representation.analysis_report import AnalysisReport

sce_ids = ["707"]
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    si_message = SQLIntakeInboundMessage(
        label=scenario.sce_id, name=scenario.name, before=scenario.before, after=scenario.after
    )

    pipeline = SQLIntakePipeline(si_message)
    se_message = pipeline.run()

    pipeline = SemanticEnginePipeline(se_message)
    se_outcome = pipeline.run()

    ar_message = AnalysisReportMessage(
        kind="SCE",
        label=si_message.label,
        name=si_message.name,
        before=se_message.before,
        after=se_message.after,
        fragments=se_outcome.fragments,
        hypotheses=se_outcome.hypotheses,
        components=se_outcome.components,
        decisions=se_outcome.decisions,
    )

    report = AnalysisReport(ar_message)
    report.show_sql_diff()
    report.show_fragments()
    report.show_hypotheses()
    report.show_components()
    report.show_decisions()
