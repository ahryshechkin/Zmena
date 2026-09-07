class MigrationForgePipeline:
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return "MigrationForgePipeline"

    def run(self):
        # statements = []

        # for selected_link in self.message:
        #     change = Change(self.message.before, self.message.after)
        #     plan = Plan(change)
        #     statements.append(plan.derive())

        return []  # statements
