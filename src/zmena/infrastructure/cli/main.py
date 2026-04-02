from zmena.application import Pipeline, ScenarioCatalog
from zmena.infrastructure import View

sce_ids = ["313"]
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    pipeline = Pipeline(scenario.before, scenario.after)
    result = pipeline.run()

    view = View(scenario)
    # view.show_report()
    # view.show_bricks(result["bricks"])
    # view.show_hypotheses(result["hypotheses"])
    # view.show_components(result["components"])
    # view.show_decisions(result["decisions"])


# print("")
# catalog.print_scenarios()
