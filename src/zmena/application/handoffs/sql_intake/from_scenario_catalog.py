from zmena.application.handoffs.sql_intake.messages.inbound import SQLIntakeInboundMessage


class ScenarioCatalogToSQLIntakeHandoff:
    def __init__(self, scenario, dialect=None, release_batch=None):
        self.scenario = scenario
        self.dialect = dialect
        self.release_batch = release_batch

    def __repr__(self):
        return "ScenarioCatalogToSQLIntakeHandoff(messages=sce,dia,rb)"

    def prepare(self):
        return SQLIntakeInboundMessage(
            label=self.scenario.sce_id,
            dialect=self.dialect,
            release_batch=self.release_batch,
            name=self.scenario.name,
            before=self.scenario.before,
            after=self.scenario.after,
        )
