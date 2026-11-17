from pathlib import Path

from zmena.domain.delta_crawler.criteria.criterion import Criterion
from zmena.domain.delta_crawler.kinds.criterion import CriterionKind


class IncludedDirectoriesCriterion(Criterion):
    def __init__(self, included_directories):
        super().__init__(CriterionKind.INCLUDED_DIRECTORIES)
        self.included_directories = included_directories

    def apply(self, entries):
        if not self.included_directories:
            return entries

        return [
            entry
            for entry in entries
            if any(
                directory.replace("\\", "/").strip("/") in Path(entry.path()).parent.as_posix()
                for directory in self.included_directories
            )
        ]
