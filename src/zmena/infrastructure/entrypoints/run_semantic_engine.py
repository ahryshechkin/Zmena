from zmena.application.messages.analysis_report import AnalysisReportMessage
from zmena.application.messages.semantic_engine import SemanticEngineMessage
from zmena.application.semantic_engine_pipeline import SemanticEnginePipeline
from zmena.infrastructure.adapters.scenario_catalog import ScenarioCatalog
from zmena.infrastructure.representation.analysis_report import AnalysisReport

sce_ids = ["312"]
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    message = SemanticEngineMessage(scenario.before.splitlines(), scenario.after.splitlines())
    pipeline = SemanticEnginePipeline(message)
    result = pipeline.run()

    message = AnalysisReportMessage(
        sce_id=scenario.sce_id,
        name=scenario.name,
        before=scenario.before.splitlines(),
        after=scenario.after.splitlines(),
        fragments=result.fragments,
        hypotheses=result.hypotheses,
        components=result.components,
        decisions=result.decisions,
    )

    report = AnalysisReport(message)
    report.show_scenario()
    report.show_fragments()
    report.show_hypotheses()
    report.show_components()
    report.show_decisions()
