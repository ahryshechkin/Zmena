from pathlib import Path

from zmena.domain.delta_crawler.criteria.criterion import Criterion
from zmena.domain.delta_crawler.kinds.criterion import CriterionKind


class ExcludedDirectoriesCriterion(Criterion):
    def __init__(self, excluded_directories):
        super().__init__(CriterionKind.EXCLUDED_DIRECTORIES)
        self.excluded_directories = excluded_directories

    def apply(self, entries):
        return [
            entry
            for entry in entries
            if not any(
                directory.replace("\\", "/").strip("/") in Path(entry.path()).parent.as_posix()
                for directory in self.excluded_directories
            )
        ]
