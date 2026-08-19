from zmena.domain.delta_crawler.criteria.excluded_extensions import ExcludedExtensionsCriterion
from zmena.domain.delta_crawler.criteria.included_extensions import IncludedExtensionsCriterion
from zmena.domain.delta_crawler.kinds.preset_kind import PresetKind
from zmena.domain.delta_crawler.presets.preset import Preset


class CriterionPreset(Preset):
    def __init__(self):
        super().__init__(PresetKind.CRITERIA)
        self.excluded_extension = ExcludedExtensionsCriterion([])
        self.included_extension = IncludedExtensionsCriterion([".sql"])

    def default(self):
        return [self.excluded_extension, self.included_extension]
