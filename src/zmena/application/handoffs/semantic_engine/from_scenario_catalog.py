from zmena.application.handoffs.semantic_engine.messages.inbound import SemanticEngineInboundMessage


class ScenarioCatalogToSemanticEngineHandoff:
    def __init__(self, scenario, dialect=None):
        self.scenario = scenario
        self.dialect = dialect

    def __repr__(self):
        return "ScenarioCatalogToSemanticEngineHandoff(messages=sce,dia)"

    def prepare(self):
        return SemanticEngineInboundMessage(
            dialect=self.dialect,
            before=self.scenario.before.splitlines(),
            after=self.scenario.after.splitlines(),
        )
