class Link:
    def __init__(self, rule_id, left, right):
        self.rule_id = rule_id
        self.left = left
        self.right = right


    def __str__(self):
        return (
            f"{self.rule_id.value:>9} | #### | {self.left} #### | {self.right}"
        )
