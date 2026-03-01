from application import Pipeline, ScenarioCatalog
from infrastructure import View


sce_ids = ["301", "304"]
catalog = ScenarioCatalog()
# for scenario in catalog.get_many(sce_ids):
for scenario in catalog.get_all():
    pipeline = Pipeline(scenario.before, scenario.after)
    result = pipeline.run()

    view = View(scenario)
    view.show_report()
    # view.show_bricks(result["bricks"])
    # view.show_links(result["links"])
    # view.show_components(result["components"])
    # view.show_decisions(result["all_links"])
    # view.show_decisions(result["selected_links"])


    # print("")
    # for case in Samples.list_cases():
    #     print(case)
