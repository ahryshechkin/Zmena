from application import Pipeline, ScenarioCatalog
from domain import Samples
from infrastructure import View


sce_ids = ["", ""]
catalog = ScenarioCatalog()
for scenario in catalog.scenarios(sce_ids):
    pipeline = Pipeline(scenario.before, scenario.after)
    result = pipeline.run()

    view = View(scenario)
    view.show_report()
    view.show_bricks(result["bricks"])


# for sample in Samples.get_pairs():
#     src = sample["src"].strip().splitlines()
#     trg = sample["trg"].strip().splitlines()
#
#     pipeline = Pipeline(src, trg)
#     result = pipeline.run()
#
#     view = View(sample)
#     view.show_report()
    # view.show_bricks(result["bricks"])
    # view.show_links(result["links"])
    # view.show_components(result["components"])
    # view.show_decisions(result["all_links"])
    # view.show_decisions(result["selected_links"])

    # print("")
    # for case in Samples.list_cases():
    #     print(case)
