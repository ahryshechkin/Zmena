class Decision:
    def __init__(self, component, heuristics):
        self.component = component
        self.heuristics = heuristics

    def __repr__(self):
        return f"Decision(chosen={len(self.chosen())})"

    def candidates(self):
        return self.component.assess(self.heuristics)

    def chosen(self):
        occupied_fragments = set()
        links = []

        for candidate in sorted(self.candidates(), reverse=True):
            left, right = candidate.fragments()
            if left in occupied_fragments or right in occupied_fragments:
                continue

            occupied_fragments.add(left)
            occupied_fragments.add(right)
            links.append(candidate)

        return links
