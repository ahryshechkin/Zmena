class ExplanationLink:
    def __init__(self, link):
        self.link = link

    def summary(self):
        left, right = self.link.bricks()

        return (
            f"Link: "
            f"{left.name} ({left.side}:{left.position})"
            f" -> "
            f"{right.name} ({right.side}:{right.position})"
        )

    def score(self):
        return self.link.score()

    def justification(self):
        return self.link.justification()
