from zmena.domain import (
    BrickService,
    ComponentService,
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
        brick_service = BrickService()
        bricks = brick_service.build(self.before, self.after)

        filtered_bricks = Filter(bricks)
        bricks_left = filtered_bricks.by_side(Side.LEFT)
        bricks_right = filtered_bricks.by_side(Side.RIGHT)
        matcher = Matcher(bricks_left.bricks, bricks_right.bricks)
        hypotheses = []
        for rule in [
            RuleDelete(),
            RuleInsert(),
            RuleName(),
            RuleOverflow(),
            RulePosition(),
            RuleSignature(),
        ]:
            hypotheses.extend(matcher.match(rule))

        component_service = ComponentService(hypotheses)
        components = component_service.compose()

        selected_links, all_links = [], []
        heuristics = [
            HeuristicCompatibility(),
            HeuristicName(),
            HeuristicPosition(),
            HeuristicSignature(),
        ]
        for component in components:
            all_links.append(component.assess(heuristics))
            decision = Decision(component, heuristics)
            selected_links.append(decision.make())

        return {
            "bricks": bricks,
            "hypotheses": hypotheses,
            "components": components,
            "all_links": all_links,
            "selected_links": selected_links,
        }
