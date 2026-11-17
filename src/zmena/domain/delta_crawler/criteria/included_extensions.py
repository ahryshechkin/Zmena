from pathlib import Path

from zmena.domain.delta_crawler.criteria.criterion import Criterion
from zmena.domain.delta_crawler.kinds.criterion import CriterionKind


class IncludedExtensionsCriterion(Criterion):
    def __init__(self, included_extensions):
        super().__init__(CriterionKind.INCLUDED_EXTENSIONS)
        self.included_extensions = included_extensions

    def apply(self, entries):
        if not self.included_extensions:
            return entries

        return [
            entry
            for entry in entries
            if any(
                Path(entry.path()).suffix.endswith(f".{extension.lstrip('.')}")
                for extension in self.included_extensions
            )
        ]
