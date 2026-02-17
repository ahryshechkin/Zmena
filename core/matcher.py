class Matcher:
    def __init__(self, *scopes):
        self.scopes = scopes


    def match(self, rule):
        return rule.apply(self.scopes)
