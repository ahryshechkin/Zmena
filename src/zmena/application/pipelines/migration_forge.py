from zmena.domain.migration_forge.core.change import Change
from zmena.domain.migration_forge.core.plan import Plan


class MigrationForgePipeline:
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return "MigrationForgePipeline"

    def run(self):
        change = Change(self.message.before, self.message.after)
        plan = Plan(change)

        return plan.derive()
