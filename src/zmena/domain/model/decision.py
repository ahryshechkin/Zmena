from zmena.domain.model.refinement import Refinement


class Decision:
    def __init__(self, component, preset):
        self.component = component
        self.preset = preset
        self.refined_links = []

    def __repr__(self):
        return f"Decision(chosen={len(self.chosen())})"

    def candidates(self):
        if not self.refined_links:
            initial_links = self.component.assess(self.preset.local())
            refinement = Refinement(initial_links)
            self.refined_links = refinement.reassess(self.preset.overall())

        return self.refined_links

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
