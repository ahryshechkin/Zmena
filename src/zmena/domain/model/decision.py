from zmena.domain.model.evaluation_scope import EvaluationScope


class Decision:
    def __init__(self, component, preset):
        self.component = component
        self.preset = preset
        self.cached_candidates = []

    def __repr__(self):
        return f"Decision(chosen={len(self.chosen())})"

    def candidates(self):
        if not self.cached_candidates:
            scope = EvaluationScope(
                heuristics=self.preset.context(),
                links=self.component.assess(self.preset.local()),
            )
            self.cached_candidates = self.component.reassess(scope)

        return self.cached_candidates

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
