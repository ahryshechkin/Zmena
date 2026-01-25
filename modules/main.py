from modules.constant import Side, Tag
from modules.engine import Engine
from modules.filter import Filter
from modules.matcher import Matcher
from modules.rule import RuleDelete, RuleName, RulePosition
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
    pairs_name = matcher.match(RuleName())
    pairs_position = matcher.match(RulePosition())
    pairs_delete = matcher.match(RuleDelete())
    view.show_pairs(pairs_name)
    view.show_pairs(pairs_position)
    view.show_pairs(pairs_delete)