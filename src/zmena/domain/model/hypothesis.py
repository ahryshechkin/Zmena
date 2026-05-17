class Hypothesis:
    def __init__(self, rule_kind, left, right):
        self.rule_kind = rule_kind
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.rule_kind.value:>9} | #### | {self.left} | #### | {self.right}"

    def __repr__(self):
        return f"Hypothesis(rule={self.rule_kind.value})"

    def key(self):
        return self.left, self.right

    def neighbor(self, fragment):
        return self.right if fragment == self.left else self.left

    def has_same_name(self):
        return self.left.same_name_as(self.right)

    def has_same_position(self):
        return self.left.same_position_as(self.right)

    def has_same_signature(self):
        return self.left.same_signature_as(self.right)

    def has_block_mismatch(self):
        return self.left.same_name_but_different_block_as(self.right)
