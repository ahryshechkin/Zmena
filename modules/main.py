from modules.decision import Decision
from modules.engine import Engine
from modules.filter import Filter
from modules.heuristic import *
from modules.matcher import Matcher
from modules.rule import *
from modules.sample import Samples
from modules.view import View


for sample in Samples.get_pairs():
    src = sample["src"].strip().splitlines()
    trg = sample["trg"].strip().splitlines()

    engine = Engine()
    engine.build_bricks(src, trg)
    view = View(sample)
    view.show_report()
    view.show_bricks(engine.bricks)

    filtered_bricks = Filter(engine.bricks)
    bricks_left = filtered_bricks.by_side(Side.LEFT)
    bricks_right = filtered_bricks.by_side(Side.RIGHT)
    matcher = Matcher(bricks_left.bricks, bricks_right.bricks)
    links = list()
    for rule in [RuleName(), RulePosition(), RuleSignature(), RuleDelete(), RuleInsert()]:
        links.extend(matcher.match(rule))
    view.show_links(links)

    components = engine.build_components(links)
    view.show_components(components)

    decisions = list()
    heuristics = [HeuristicName(), HeuristicPosition()]
    for component in components:
        decision = Decision(component, heuristics)
        decisions.append(decision.make())

    view.show_decisions(decisions)



    # print("")
    # for case in Samples.list_cases():
    #     print(case)
