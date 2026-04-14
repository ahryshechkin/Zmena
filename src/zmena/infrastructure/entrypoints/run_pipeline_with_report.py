from zmena.application import Pipeline, ScenarioCatalog
from zmena.infrastructure.representation.report import Report

sce_ids = ["313"]
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    pipeline = Pipeline(scenario.before, scenario.after)
    result = pipeline.run()

    report = Report(scenario)
    report.show_scenario()
    # report.show_bricks(result["bricks"])
    report.show_hypotheses(result["hypotheses"])
    # report.show_components(result["components"])
    report.show_decisions(result["decisions"])
