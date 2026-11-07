from zmena.application.handoffs.sql_intake.messages.inbound import SQLIntakeInboundMessage
from zmena.infrastructure.project_directory import ProjectDirectory


class ScenarioCatalogToSQLIntakeHandoff:
    def __init__(self, scenario, batch, dialect):
        self.scenario = scenario
        self.batch = batch
        self.dialect = dialect

    def __repr__(self):
        return "ScenarioCatalogToSQLIntakeHandoff(messages=sce,bat,dia)"

    def prepare(self):
        directory = ProjectDirectory()
        batch_path = directory.releases() / self.batch.partition_path()

        return SQLIntakeInboundMessage(
            label=self.scenario.sce_id,
            batch_path=batch_path,
            dialect=self.dialect,
            name=self.scenario.name,
            before=self.scenario.before,
            after=self.scenario.after,
        )
