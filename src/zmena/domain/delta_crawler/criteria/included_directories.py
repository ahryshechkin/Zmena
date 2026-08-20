from zmena.domain.delta_crawler.criteria.criterion import Criterion
from zmena.domain.delta_crawler.kinds.criterion_kind import CriterionKind


class IncludedDirectoriesCriterion(Criterion):
    def __init__(self, included_directories):
        super().__init__(CriterionKind.INCLUDED_DIRECTORIES)
        self.included_directories = included_directories

    def apply(self, paths):
        return [
            path
            for path in paths
            if any(directory in path for directory in self.included_directories)
        ]
