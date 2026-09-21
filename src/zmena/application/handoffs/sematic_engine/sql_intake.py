from zmena.application.messages.inbound.semantic_engine import SemanticEngineInboundMessage


class SQLIntakeToSemanticEngineHandoff:
    def __init__(self, sio_message):
        self.sio_message = sio_message

    def __repr__(self):
        return "SQLIntakeToSemanticEngineHandoff(messages=sce)"

    def prepare(self):
        return SemanticEngineInboundMessage(
            before=self.sio_message.before, after=self.sio_message.after
        )
