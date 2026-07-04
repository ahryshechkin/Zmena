from zmena.application import AnalysisPipeline, SQLIntakePipeline
from zmena.infrastructure.adapters.scenario_catalog import ScenarioCatalog
from zmena.infrastructure.representation.analysis_report import AnalysisReport

sce_ids = ["771"]
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    sqli = SQLIntakePipeline(scenario.before, scenario.after)
    before, after = sqli.run()

    sme = AnalysisPipeline(before, after)
    result = sme.run()

    report = AnalysisReport(scenario, result)
    # report.show_scenario()
    report.show_fragments()
    report.show_hypotheses()
    report.show_components()
    report.show_decisions()
