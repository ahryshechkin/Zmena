from modules.constant import Side, Tag
from modules.engine import Engine
from modules.filter import Filter
from modules.matcher import Matcher
from modules.rule import RuleDelete, RuleInsert, RuleName, RulePosition
from modules.sample import Samples
from modules.view import View


engine = Engine()
for sample in Samples.get_pairs():
    src = sample["src"].strip().splitlines()
    trg = sample["trg"].strip().splitlines()
    engine.run(src, trg)
    view = View(sample)
    view.show_report()
    view.show_bricks(engine.bricks)
    filtered_bricks = Filter(engine.bricks)
    left_bricks = filtered_bricks.by_side(Side.LEFT)
    right_bricks = filtered_bricks.by_side(Side.RIGHT)
    matcher = Matcher(left_bricks.bricks, right_bricks.bricks)
    for rule in [RuleDelete(), RuleInsert(), RuleName(), RulePosition()]:
        pairs = matcher.match(rule)
        view.show_pairs(pairs)