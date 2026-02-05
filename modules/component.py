class Component:
    def __init__(self):
        self.links = set()
        self.bricks = set()


    def add(self, link):
        self.links.add(link)
        self.bricks.add(link.left)
        self.bricks.add(link.right)


    def evaluate(self, heuristics):
        scores = dict()
        for link in self.links:
            score = 0
            for heuristic in heuristics:
                score += heuristic.score(link)
            scores[link] = score

        return scores
