from zmena.application.messages.inbound.sql_intake import SQLIntakeInboundMessage


class ScenarioCatalogToSQLIntakeHandoff:
    def __init__(self, scenario):
        self.scenario = scenario

    def __repr__(self):
        return "ScenarioCatalogToSQLIntakeHandoff(messages=sce)"

    def prepare(self):
        return SQLIntakeInboundMessage(
            label=self.scenario.sce_id,
            name=self.scenario.name,
            before=self.scenario.before,
            after=self.scenario.after,
        )
