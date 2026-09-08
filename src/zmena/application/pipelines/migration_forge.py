class MigrationForgePipeline:
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return "MigrationForgePipeline"

    def run(self):
        # statements = []

        # before = None
        # after = Snapshot(
        #     name=right.name, data_type=right.data_type, nullable=right.constraint != "NOT NULL"
        # )

        # for selected_link in self.message:
        #     change = Change(self.message.before, self.message.after)
        #     plan = Plan(change)
        #     statements.append(plan.derive())

        return []  # statements
