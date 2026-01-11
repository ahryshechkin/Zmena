from modules.engine import Engine
from modules.filter import Filter
from modules.sample import Samples
from modules.view import View


engine = Engine()
for sample in Samples.get_pairs():
    src = sample["src"].strip().splitlines()
    trg = sample["trg"].strip().splitlines()
    engine.run(src, trg)
    view = View(sample)
    view.show_report()
    brick_filter = Filter(engine.bricks)
    view.show_bricks(engine.bricks)
    result = brick_filter.by_tag("replace").by_side("R").result()
    view.show_bricks(result)
