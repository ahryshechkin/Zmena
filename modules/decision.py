class Decision:
    def __init__(self, component, heuristics):
        self.component = component
        self.heuristics = heuristics


    def make(self):
        result = list()
        used_bricks = set()

        scored_links = self.component.evaluate(self.heuristics)
        for candidate in sorted(scored_links, reverse=True):
            if candidate.left not in used_bricks and candidate.right not in used_bricks:
                used_bricks.add(candidate.left)
                used_bricks.add(candidate.right)
                result.append(candidate)

        return result
