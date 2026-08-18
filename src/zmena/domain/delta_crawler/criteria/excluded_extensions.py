from zmena.domain.delta_crawler.criteria.criterion import Criterion
from zmena.domain.delta_crawler.kinds.criterion_kind import CriterionKind


class ExcludedExtensionsCriterion(Criterion):
    def __init__(self, excluded_extensions):
        super().__init__(CriterionKind.EXCLUDED_EXTENSIONS)
        self.excluded_extensions = excluded_extensions

    def apply(self, paths):
        return [
            path
            for path in paths
            if not any(path.endswith(extension) for extension in self.excluded_extensions)
        ]
