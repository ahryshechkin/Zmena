from modules.engine import Engine
from modules.filter import Filter
from modules.matcher import Matcher
from modules.rule import NameRule, PositionRule
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
    # result = brick_filter.by_side("L").result()
    # view.show_bricks(result)
    rule = NameRule()
    matcher = Matcher(engine.bricks, engine.bricks)
    pairs_name = matcher.match(rule)
    print("")
    for pair in pairs_name:
        print(f"{pair[0]} <=> {pair[1]}")
    pairs_position = matcher.match(PositionRule())
    print("")
    for pair in pairs_position:
        print(f"{pair[0]} <=> {pair[1]}")