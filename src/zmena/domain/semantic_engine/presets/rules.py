from zmena.domain.semantic_engine.presets.preset import Preset
from zmena.domain.semantic_engine.rules.delete import DeleteRule
from zmena.domain.semantic_engine.rules.imbalance import ImbalanceRule
from zmena.domain.semantic_engine.rules.insert import InsertRule
from zmena.domain.semantic_engine.rules.name import NameRule
from zmena.domain.semantic_engine.rules.position import PositionRule
from zmena.domain.semantic_engine.rules.signature import SignatureRule
from zmena.domain.semantic_engine.types.preset_kind import PresetKind


class RulePreset(Preset):
    def __init__(self):
        super().__init__(PresetKind.RULES)
        self.delete = DeleteRule()
        self.imbalance = ImbalanceRule()
        self.insert = InsertRule()
        self.name = NameRule()
        self.position = PositionRule()
        self.signature = SignatureRule()

    def default(self):
        return [
            self.delete,
            self.imbalance,
            self.insert,
            self.name,
            self.position,
            self.signature,
        ]
