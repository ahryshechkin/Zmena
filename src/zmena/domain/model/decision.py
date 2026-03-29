class Decision:
    def __init__(self, component, heuristics):
        self.component = component
        self.heuristics = heuristics

    def make(self):
        used_bricks = set()
        links = []

        candidates = self.component.assess(self.heuristics)
        for candidate in sorted(candidates, reverse=True):
            if candidate.conflicts_with(used_bricks):
                continue

            left, right = candidate.bricks()
            used_bricks.add(left)
            used_bricks.add(right)
            links.append(candidate)

        return links
