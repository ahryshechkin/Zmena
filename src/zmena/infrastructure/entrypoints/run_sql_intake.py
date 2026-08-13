from zmena.application.messages.analysis_report import AnalysisReportMessage
from zmena.application.messages.sql_intake import SQLIntakeMessage
from zmena.application.semantic_engine_pipeline import SemanticEnginePipeline
from zmena.application.sql_intake_pipeline import SQLIntakePipeline
from zmena.infrastructure.adapters.scenario_catalog import ScenarioCatalog
from zmena.infrastructure.representation.analysis_report import AnalysisReport

sce_ids = ["707"]
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    si_message = SQLIntakeMessage(scenario.sce_id, scenario.name, scenario.before, scenario.after)

    pipeline = SQLIntakePipeline(si_message)
    se_message = pipeline.run()

    pipeline = SemanticEnginePipeline(se_message)
    result = pipeline.run()

    ar_message = AnalysisReportMessage(
        kind="SCE",
        label=si_message.label,
        name=si_message.name,
        before=se_message.before,
        after=se_message.after,
        fragments=result.fragments,
        hypotheses=result.hypotheses,
        components=result.components,
        decisions=result.decisions,
    )

    report = AnalysisReport(ar_message)
    report.show_scenario()
    report.show_fragments()
    report.show_hypotheses()
    report.show_components()
    report.show_decisions()
