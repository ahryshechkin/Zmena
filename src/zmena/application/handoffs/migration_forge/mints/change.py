from zmena.domain.migration_forge.core.change import Change


class ChangeMint:
    def __init__(self, mint):
        self.mint = mint

    def __repr__(self):
        return "ChangeMint(mints=change,snapshot)"

    def issue(self, decisions):
        changes = []
        for decision in decisions:
            for winner in decision.winners():
                change = Change(
                    before=self.mint.issue(winner.left),
                    after=self.mint.issue(winner.right),
                )
                changes.append(change)

        return changes
