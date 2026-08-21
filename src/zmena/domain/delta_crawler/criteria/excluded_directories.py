from pathlib import Path

from zmena.domain.delta_crawler.criteria.criterion import Criterion
from zmena.domain.delta_crawler.kinds.criterion_kind import CriterionKind


class ExcludedDirectoriesCriterion(Criterion):
    def __init__(self, excluded_directories):
        super().__init__(CriterionKind.EXCLUDED_DIRECTORIES)
        self.excluded_directories = excluded_directories

    def apply(self, paths):
        return [
            path
            for path in paths
            if not any(
                directory in Path(path).parent.as_posix() for directory in self.excluded_directories
            )
        ]
