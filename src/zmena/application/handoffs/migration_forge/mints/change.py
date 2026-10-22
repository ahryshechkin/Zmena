from zmena.domain.migration_forge.core.change import Change


class ChangeMint:
    def __init__(self, mint):
        self.mint = mint

    def __repr__(self):
        return "ChangeMint(mints=change,snapshot)"

    def issue(self, tab_name, decisions):
        changes = []
        for decision in decisions:
            for winner in decision.winners():
                change = Change(
                    tab_name, self.mint.issue(winner.left), self.mint.issue(winner.right)
                )
                changes.append(change)

        return changes
