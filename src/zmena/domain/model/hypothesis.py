class Hypothesis:
    def __init__(self, rule_label, left, right):
        self.rule_label = rule_label
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.rule_label.value:>9} | #### | {self.left} #### | {self.right}"

    def __repr__(self):
        return f"Hypothesis(rule={self.rule_label.value})"

    def key(self):
        return self.left, self.right

    def signature_mismatch(self):
        return not self.left.same_signature_as(self.right)
