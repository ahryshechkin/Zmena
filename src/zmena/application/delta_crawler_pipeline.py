from zmena.application.messages.sql_intake import SQLIntakeMessage
from zmena.domain.delta_crawler.tag_record import TagRecord


class DeltaCrawlerPipeline:
    def __init__(self, commit_from, commit_to):
        self.commit_from = commit_from
        self.commit_to = commit_to

    def __repr__(self):
        return f"DeltaCrawlerPipeline(commit_from={self.commit_from},commit_to={self.commit_to})"

    def run(self, command):
        record = TagRecord(command.show_tag(self.commit_to))
        annotation = record.annotation()

        messages = []
        for path in command.diff(self.commit_from, self.commit_to):
            before = command.show(self.commit_from, path)
            after = command.show(self.commit_to, path)
            message = SQLIntakeMessage(path, annotation, before, after)
            messages.append(message)

        return messages
