from zmena.application.messages.analysis_report import AnalysisReportMessage
from zmena.application.messages.inbound.semantic_engine import SemanticEngineInboundMessage
from zmena.application.pipelines.semantic_engine import SemanticEnginePipeline
from zmena.infrastructure.adapters.scenario_catalog import ScenarioCatalog
from zmena.infrastructure.representation.analysis_report import AnalysisReport

sce_ids = ["403"]
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    sei_message = SemanticEngineInboundMessage(
        before=scenario.before.splitlines(), after=scenario.after.splitlines()
    )

    pipeline = SemanticEnginePipeline(sei_message)
    se_outcome = pipeline.run()

    ar_message = AnalysisReportMessage(
        kind="SCE",
        label=scenario.sce_id,
        name=scenario.name,
        before=scenario.before.splitlines(),
        after=scenario.after.splitlines(),
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
