from application import Pipeline
from domain import Samples
from infrastructure import View


for sample in Samples.get_pairs():
    src = sample["src"].strip().splitlines()
    trg = sample["trg"].strip().splitlines()

    pipeline = Pipeline(src, trg)
    result = pipeline.run()

    view = View(sample)
    view.show_report()
    view.show_bricks(result[0])
    view.show_links(result[1])
    view.show_components(result[2])
    view.show_decisions(result[3])
    view.show_decisions(result[4])

    # print("")
    # for case in Samples.list_cases():
    #     print(case)
