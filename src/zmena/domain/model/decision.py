class Decision:
    def __init__(self, links):
        self.links = links

    def __repr__(self):
        return f"Decision(links={len(self.links)})"

    def candidates(self):
        return self.links

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
