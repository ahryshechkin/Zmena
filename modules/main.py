from modules.engine import Engine
from modules.filter import Filter
from modules.matcher import Matcher
from modules.rule import RuleName, RulePosition
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
    matcher = Matcher(engine.bricks, engine.bricks)
    pairs_name = matcher.match(RuleName())
    pairs_position = matcher.match(RulePosition())
    view.show_pairs(pairs_name)
    print("")
    # for pair in pairs_name:
    #     print(f"{pair[0]} <=> {pair[1]}")
    # print("")
    # for pair in pairs_position:
    #     print(f"{pair[0]} <=> {pair[1]}")