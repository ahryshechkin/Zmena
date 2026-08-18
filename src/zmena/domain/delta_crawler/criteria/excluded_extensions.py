from zmena.domain.delta_crawler.criteria.criterion import Criterion


class ExcludedExtensionsCriterion(Criterion):
    def __init__(self, excluded_extensions):
        super().__init__("dad")
        self.excluded_extensions = excluded_extensions

    def apply(self, paths):
        return [
            path
            for path in paths
            if not any(path.endswith(extension) for extension in self.excluded_extensions)
        ]
