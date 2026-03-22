class Decision:
    def __init__(self, component, heuristics):
        self.component = component
        self.heuristics = heuristics

    def make(self):
        selected_links = []
        used_bricks = set()

        links = self.component.assess(self.heuristics)
        for candidate in sorted(links, reverse=True):
            if candidate.conflicts_with(used_bricks):
                continue

            left, right = candidate.bricks()
            used_bricks.add(left)
            used_bricks.add(right)
            selected_links.append(candidate)

        return selected_links
