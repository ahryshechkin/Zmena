from zmena.application.messages.outbound.delta_crawler import DeltaCrawlerOutboundMessage
from zmena.domain.delta_crawler.core.revision_paths import RevisionPaths
from zmena.domain.delta_crawler.core.tag_record import TagRecord


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
            message = DeltaCrawlerOutboundMessage(
                label=record.name(), name=record.annotation(), before=before, after=after
            )
            messages.append(message)

        return messages
