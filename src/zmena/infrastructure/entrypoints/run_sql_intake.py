from zmena.application.messages.sql_intake import SQLIntakeMessage
from zmena.application.semantic_engine_pipeline import SemanticEnginePipeline
from zmena.application.sql_intake_pipeline import SQLIntakePipeline
from zmena.infrastructure.adapters.scenario_catalog import ScenarioCatalog
from zmena.infrastructure.representation.analysis_report import AnalysisReport

sce_ids = ["707"]
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    message = SQLIntakeMessage("", scenario.before, scenario.after)
    pipeline = SQLIntakePipeline(message)
    before, after = pipeline.run()

    pipeline = SemanticEnginePipeline(before, after)
    result = pipeline.run()

    scenario.before, scenario.after = before, after
    report = AnalysisReport(scenario, result)
    report.show_scenario()
    report.show_fragments()
    report.show_hypotheses()
    report.show_components()
    report.show_decisions()
