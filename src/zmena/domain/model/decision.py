class Decision:
    def __init__(self, component, heuristics):
        self.component = component
        self.heuristics = heuristics

    def make(self):
        selected_links = []
        used_bricks = set()

        scored_links = self.component.assess(self.heuristics)
        # links = self.component.assess2(self.heuristics)
        for candidate in sorted(scored_links, reverse=True):
            if candidate.conflicts_with(used_bricks):
                continue

            left, right = candidate.bricks()
            used_bricks.add(left)
            used_bricks.add(right)
            selected_links.append(candidate)

        return selected_links
