from modules.engine import Engine
from modules.filter import Filter
from modules.matcher import Matcher
from modules.rule import *
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

    links = list()
    for rule in [RuleName(), RulePosition(), RuleSignature(), RuleDelete(), RuleInsert()]:
        links.extend(matcher.match(rule))

    view.show_links(links)