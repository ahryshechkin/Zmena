from zmena.application.messages.analysis_report import AnalysisReportMessage
from zmena.application.messages.semantic_engine import SemanticEngineMessage
from zmena.application.pipelines.semantic_engine import SemanticEnginePipeline
from zmena.infrastructure.adapters.scenario_catalog import ScenarioCatalog
from zmena.infrastructure.representation.analysis_report import AnalysisReport

sce_ids = ["403"]
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    se_message = SemanticEngineMessage(scenario.before.splitlines(), scenario.after.splitlines())

    pipeline = SemanticEnginePipeline(se_message)
    result = pipeline.run()

    ar_message = AnalysisReportMessage(
        kind="SCE",
        label=scenario.sce_id,
        name=scenario.name,
        before=scenario.before.splitlines(),
        after=scenario.after.splitlines(),
        fragments=result.fragments,
        hypotheses=result.hypotheses,
        components=result.components,
        decisions=result.decisions,
    )

    report = AnalysisReport(ar_message)
    report.show_sql_diff()
    report.show_fragments()
    report.show_hypotheses()
    report.show_components()
    report.show_decisions()
