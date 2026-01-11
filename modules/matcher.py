class Matcher:
    def __init__(self, left, right):
        self.left = left
        self.right = right


    def match(self, rule):
        pairs = []

        for left in self.left:
            for right in self.right:
                if left != right and rule.match(left, right):
                    pairs.append([left, right])

        return pairs