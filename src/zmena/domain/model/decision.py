from zmena.domain.model.evaluation_context import EvaluationContext


class Decision:
    def __init__(self, component, preset):
        self.component = component
        self.preset = preset
        self.final_candidates = []

    def __repr__(self):
        return f"Decision(chosen={len(self.chosen())})"

    def candidates(self):
        if not self.final_candidates:
            draft_candidates = self.component.assess(self.preset.local())
            context = EvaluationContext(self.preset.overall())
            self.final_candidates = context.reassess(draft_candidates)

        return self.final_candidates

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
