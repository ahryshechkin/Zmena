from application import Engine
from domain import *


class Pipeline:
    def __init__(self, before, after):
        self.before = before
        self.after = after


    def run(self):
        engine = Engine()
        engine.build_bricks(self.before, self.after)

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

        return {
            "bricks": engine.bricks,
            "links": links,
            "components": components,
            "all_links": all_links,
            "selected_links": selected_links,
        }