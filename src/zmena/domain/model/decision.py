class Decision:
    def __init__(self, component, heuristics):
        self.component = component
        self.heuristics = heuristics

    def candidates(self):
        return self.component.assess(self.heuristics)

    def chosen(self):
        used_bricks = set()
        links = []

        for candidate in sorted(self.candidates(), reverse=True):
            if candidate.conflicts_with(used_bricks):
                continue

            left, right = candidate.bricks()
            used_bricks.add(left)
            used_bricks.add(right)
            links.append(candidate)

        return links
