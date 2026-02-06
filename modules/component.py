from modules.link import ScoredLink


class Component:
    def __init__(self):
        self.links = set()
        self.bricks = set()


    def add(self, link):
        self.links.add(link)
        self.bricks.add(link.left)
        self.bricks.add(link.right)


    def evaluate(self, heuristics):
        scored_links = list()
        for link in self.links:
            score = 0
            for heuristic in heuristics:
                score += heuristic.score(link)
            scored_links.append(ScoredLink(score, link))

        return scored_links
