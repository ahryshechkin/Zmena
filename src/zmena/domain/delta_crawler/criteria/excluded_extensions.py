from pathlib import Path

from zmena.domain.delta_crawler.criteria.criterion import Criterion
from zmena.domain.delta_crawler.kinds.criterion import CriterionKind


class ExcludedExtensionsCriterion(Criterion):
    def __init__(self, excluded_extensions):
        super().__init__(CriterionKind.EXCLUDED_EXTENSIONS)
        self.excluded_extensions = excluded_extensions

    def apply(self, entries):
        return [
            entry
            for entry in entries
            if not any(
                Path(entry.path()).suffix.endswith(f".{extension.lstrip('.')}")
                for extension in self.excluded_extensions
            )
        ]
