from zmena.domain.presets.preset import Preset
from zmena.domain.rules.delete import DeleteRule
from zmena.domain.rules.imbalance import ImbalanceRule
from zmena.domain.rules.insert import InsertRule
from zmena.domain.rules.name import NameRule
from zmena.domain.rules.position import PositionRule
from zmena.domain.rules.signature import SignatureRule
from zmena.domain.types.preset_kind import PresetKind


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
