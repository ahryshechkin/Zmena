from zmena.application.handoffs.sql_intake.messages.inbound import SQLIntakeInboundMessage


class ScenarioCatalogToSQLIntakeHandoff:
    def __init__(self, scenario, batch=None, dialect=None):
        self.scenario = scenario
        self.batch = batch
        self.dialect = dialect

    def __repr__(self):
        return "ScenarioCatalogToSQLIntakeHandoff(messages=sce,bat,dia)"

    def prepare(self):
        return SQLIntakeInboundMessage(
            label=self.scenario.sce_id,
            batch=self.batch,
            dialect=self.dialect,
            name=self.scenario.name,
            before=self.scenario.before,
            after=self.scenario.after,
        )
