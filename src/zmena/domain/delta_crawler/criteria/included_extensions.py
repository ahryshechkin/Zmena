from zmena.domain.delta_crawler.criteria.criterion import Criterion
from zmena.domain.delta_crawler.kinds.criterion_kind import CriterionKind


class IncludedExtensionsCriterion(Criterion):
    def __init__(self, included_extensions):
        super().__init__(CriterionKind.INCLUDED_EXTENSIONS)
        self.included_extensions = included_extensions

    def apply(self, paths):
        return [
            path
            for path in paths
            if any(path.endswith(extension) for extension in self.included_extensions)
        ]
