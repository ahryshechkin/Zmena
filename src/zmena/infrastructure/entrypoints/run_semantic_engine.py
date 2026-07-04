from zmena.application import SemanticEnginePipeline
from zmena.infrastructure.adapters.scenario_catalog import ScenarioCatalog
from zmena.infrastructure.representation.analysis_report import AnalysisReport

sce_ids = ["011"]
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    pipeline = SemanticEnginePipeline(scenario.before, scenario.after)
    result = pipeline.run()

    report = AnalysisReport(scenario, result)
    report.show_scenario()
    report.show_fragments()
    report.show_hypotheses()
    report.show_components()
    report.show_decisions()
