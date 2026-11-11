from zmena.application.handoffs.delta_crawler.messages.outbound import DeltaCrawlerOutboundMessage
from zmena.application.kinds.pipeline import PipelineKind
from zmena.application.pipelines.pipeline import Pipeline
from zmena.domain.delta_crawler.core.path_sieve import PathSieve
from zmena.domain.delta_crawler.core.tag_header import TagHeader


class DeltaCrawlerPipeline(Pipeline):
    def __init__(self, message):
        super().__init__(PipelineKind.DELTA_CRAWLER)
        self.message = message

    def run(self):
        command = self.message.command
        sieve = PathSieve(command.diff(self.message.commit_from, self.message.commit_to))
        header = TagHeader(command.show_tag(self.message.commit_to))

        messages = []
        for path in sieve.filter():
            before = command.show(self.message.commit_from, path)
            after = command.show(self.message.commit_to, path)
            message = DeltaCrawlerOutboundMessage(
                cmt_id=header.name(),
                dialect=self.message.dialect,
                release_batch=self.message.release_batch,
                name=header.summary(),
                before=before,
                after=after,
            )
            messages.append(message)

        return messages
