from core.constant import Side
from core.decision import Decision
from core.engine import Engine
from core.filter import Filter
from heuristics import HeuristicCompatibility, HeuristicName, HeuristicPosition, HeuristicSignature
from core.matcher import Matcher
from rules import RuleName, RulePosition, RuleSignature, RuleDelete, RuleInsert, RuleOverflow
from core.sample import Samples
from core.view import View


for sample in Samples.get_pairs():
    src = sample["src"].strip().splitlines()
    trg = sample["trg"].strip().splitlines()

    engine = Engine()
    engine.build_bricks(src, trg)

    filtered_bricks = Filter(engine.bricks)
    bricks_left = filtered_bricks.by_side(Side.LEFT)
    bricks_right = filtered_bricks.by_side(Side.RIGHT)
    matcher = Matcher(bricks_left.bricks, bricks_right.bricks)
    links = list()
    for rule in [RuleName(), RulePosition(), RuleSignature(), RuleDelete(), RuleInsert(), RuleOverflow()]:
        links.extend(matcher.match(rule))

    components = engine.build_components(links)

    selected_links, all_links = list(), list()
    heuristics = [HeuristicCompatibility(), HeuristicName(), HeuristicPosition(), HeuristicSignature()]
    for component in components:
        all_links.append(component.evaluate(heuristics))
        decision = Decision(component, heuristics)
        selected_links.append(decision.make())

    view = View(sample)
    view.show_report()
    view.show_bricks(engine.bricks)
    view.show_links(links)
    view.show_components(components)
    view.show_decisions(all_links)
    view.show_decisions(selected_links)

    # print("")
    # for case in Samples.list_cases():
    #     print(case)
