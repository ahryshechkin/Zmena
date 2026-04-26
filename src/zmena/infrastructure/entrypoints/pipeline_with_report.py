from zmena.application import AnalysisPipeline, ScenarioCatalog
from zmena.infrastructure.representation.report import Report

sce_ids = ["313"]
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    analysis_pipeline = AnalysisPipeline(scenario.before, scenario.after)
    result = analysis_pipeline.run()

    report = Report(scenario)
    report.show_scenario()
    report.show_fragments(result["fragments"])
    report.show_hypotheses(result["hypotheses"])
    report.show_components(result["components"])
    report.show_decisions(result["decisions"])
