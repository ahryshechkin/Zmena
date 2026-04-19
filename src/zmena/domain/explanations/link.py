class ExplanationLink:
    def __init__(self, link):
        self.link = link

    def formatted_header(self):
        left, right = self.link.fragments()

        return (
            f"Link: "
            f"{left.name} ({left.side}:{left.position})"
            f" -> "
            f"{right.name} ({right.side}:{right.position})"
        )

    def formatted_score(self):
        return f"Score: {self.link.score()}"

    def evidences(self):
        return self.link.justification()
