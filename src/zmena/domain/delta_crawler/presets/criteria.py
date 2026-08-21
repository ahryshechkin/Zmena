from zmena.domain.delta_crawler.criteria.excluded_directories import ExcludedDirectoriesCriterion
from zmena.domain.delta_crawler.criteria.excluded_extensions import ExcludedExtensionsCriterion
from zmena.domain.delta_crawler.criteria.included_directories import IncludedDirectoriesCriterion
from zmena.domain.delta_crawler.criteria.included_extensions import IncludedExtensionsCriterion
from zmena.domain.delta_crawler.kinds.preset_kind import PresetKind
from zmena.domain.delta_crawler.presets.preset import Preset


class CriterionPreset(Preset):
    def __init__(self):
        super().__init__(PresetKind.CRITERIA)
        self.excluded_directories = ExcludedDirectoriesCriterion([])
        self.excluded_extensions = ExcludedExtensionsCriterion([])
        self.included_directories = IncludedDirectoriesCriterion([])
        self.included_extensions = IncludedExtensionsCriterion([])

    def default(self):
        return [
            self.excluded_directories,
            self.excluded_extensions,
            self.included_directories,
            self.included_extensions,
        ]
