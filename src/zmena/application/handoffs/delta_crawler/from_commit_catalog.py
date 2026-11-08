from zmena.application.handoffs.delta_crawler.messages.inbound import DeltaCrawlerInboundMessage
from zmena.infrastructure.adapters.commands.git import GitCommand
from zmena.infrastructure.project_directory import ProjectDirectory


class CommitCatalogToDeltaCrawlerHandoff:
    def __init__(self, commit_from, commit_to, batch=None, dialect=None):
        self.commit_from = commit_from
        self.commit_to = commit_to
        self.batch = batch
        self.dialect = dialect

    def __repr__(self):
        return "CommitCatalogToDeltaCrawlerHandoff(messages=cmt)"

    def prepare(self):
        directory = ProjectDirectory()
        command = GitCommand(directory.demo_repo())

        return DeltaCrawlerInboundMessage(
            command=command,
            batch=self.batch,
            dialect=self.dialect,
            commit_from=self.commit_from,
            commit_to=self.commit_to,
        )
