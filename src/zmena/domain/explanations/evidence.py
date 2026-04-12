from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from zmena.domain.model.hypothesis import Hypothesis


@dataclass
class Evidence:
    hypothesis: Hypothesis
    feature: float
    weight: float
    reason: str

    def __repr__(self):
        return f"Evidence(feature={self.feature},weight={self.weight},reason={self.reason})"

    def score(self):
        return self.feature * self.weight
