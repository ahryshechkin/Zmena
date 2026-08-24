from zmena.application.messages.sql_intake import SQLIntakeMessage
from zmena.domain.delta_crawler.revision_paths import RevisionPaths
from zmena.domain.delta_crawler.tag_record import TagRecord


class DeltaCrawlerPipeline:
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return "DeltaCrawlerPipeline"

    def run(self, command):
        messages = []

        record = TagRecord(command.show_tag(self.message.commit_to))
        revision_paths = RevisionPaths(
            command.diff(self.message.commit_from, self.message.commit_to)
        )
        for path in revision_paths.filter():
            before = command.show(self.message.commit_from, path)
            after = command.show(self.message.commit_to, path)
            message = SQLIntakeMessage(record.name(), record.annotation(), before, after)
            messages.append(message)

        return messages
