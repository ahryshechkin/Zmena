from zmena.application import Engine
from zmena.domain import (
    Decision,
    Filter,
    HeuristicCompatibility,
    HeuristicName,
    HeuristicPosition,
    HeuristicSignature,
    Matcher,
    RuleDelete,
    RuleInsert,
    RuleName,
    RuleOverflow,
    RulePosition,
    RuleSignature,
    Side,
)


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
        links = []
        for rule in [
            RuleDelete(),
            RuleInsert(),
            RuleName(),
            RuleOverflow(),
            RulePosition(),
            RuleSignature(),
        ]:
            links.extend(matcher.match(rule))

        components = engine.build_components(links)

        selected_links, all_links = [], []
        heuristics = [
            HeuristicCompatibility(),
            HeuristicName(),
            HeuristicPosition(),
            HeuristicSignature(),
        ]
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
