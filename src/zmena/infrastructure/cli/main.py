from zmena.application import Pipeline, ScenarioCatalog
from zmena.infrastructure.view.brick_report import BrickReport
from zmena.infrastructure.view.component_report import ComponentReport
from zmena.infrastructure.view.hypothesis_report import HypothesisReport
from zmena.infrastructure.view.view import View

sce_ids = ["313"]
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    pipeline = Pipeline(scenario.before, scenario.after)
    result = pipeline.run()

    BrickReport(result["bricks"]).render()
    HypothesisReport(result["hypotheses"]).render()
    ComponentReport(result["components"]).render()

    view = View(scenario)
    # view.show_report()
    # view.show_bricks(result["bricks"])
    # view.show_hypotheses(result["hypotheses"])
    view.show_components(result["components"])
    view.show_decisions(result["decisions"])


# print("")
# catalog.print_scenarios()
