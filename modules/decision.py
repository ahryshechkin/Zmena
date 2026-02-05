class Decision:
    def __init__(self, component, heuristics):
        self.component = component
        self.heuristics = heuristics


    def make(self):
        result = dict()
        used_bricks = set()

        scores = self.component.evaluate(self.heuristics)
        sorted_links = sorted(scores, key=scores.get, reverse=True)
        for link in sorted_links:
            if link.left not in used_bricks and link.right not in used_bricks:
                used_bricks.add(link.left)
                used_bricks.add(link.right)
                result[link] = scores[link]

        return result
