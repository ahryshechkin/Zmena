class Decision:
    def __init__(self, component, heuristics):
        self.component = component
        self.heuristics = heuristics


    def make(self):
        scores = dict()
        for link in self.component.links:
            score = 0
            for heuristic in self.heuristics:
                score += heuristic.score(link)
            scores[link] = score

        result = dict()
        sorted_links = sorted(scores, key=scores.get, reverse=True)
        used_bricks = set()
        for link in sorted_links:
            if link.left not in used_bricks and link.right not in used_bricks:
                used_bricks.add(link.left)
                used_bricks.add(link.right)
                result[link] = scores[link]

        return result
