class Decision:
    def __init__(self, component, heuristics):
        self.component = component
        self.heuristics = heuristics


    def make(self):
        result = list()
        used_bricks = set()

        scored_links = self.component.evaluate(self.heuristics)
        for scored_link in sorted(scored_links, reverse=True):
            link = scored_link.link
            if link.left not in used_bricks and link.right not in used_bricks:
                used_bricks.add(link.left)
                used_bricks.add(link.right)
                result.append(scored_link)

        return result
