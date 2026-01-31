class Link:
    def __init__(self, rule_name, left, right):
        self.rule_name = rule_name
        self.left = left
        self.right = right


    def __str__(self):
        return (
            f"{self.rule_name:12} | {self.left} <==> | {self.right}"
        )
