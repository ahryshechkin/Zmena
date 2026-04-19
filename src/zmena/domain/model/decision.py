class Decision:
    def __init__(self, component, heuristics):
        self.component = component
        self.heuristics = heuristics

    def __repr__(self):
        return f"Decision(chosen={len(self.chosen())})"

    def candidates(self):
        return self.component.assess(self.heuristics)

    def chosen(self):
        used_fragments = set()
        links = []

        for candidate in sorted(self.candidates(), reverse=True):
            if candidate.conflicts_with(used_fragments):
                continue

            left, right = candidate.fragments()
            used_fragments.add(left)
            used_fragments.add(right)
            links.append(candidate)

        return links
