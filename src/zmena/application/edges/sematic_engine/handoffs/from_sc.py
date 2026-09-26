from zmena.application.edges.sematic_engine.messages.inbound import SemanticEngineInboundMessage


class ScenarioCatalogToSemanticEngineHandoff:
    def __init__(self, scenario):
        self.scenario = scenario

    def __repr__(self):
        return "ScenarioCatalogToSemanticEngineHandoff(messages=sce)"

    def prepare(self):
        return SemanticEngineInboundMessage(
            before=self.scenario.before.splitlines(), after=self.scenario.after.splitlines()
        )
