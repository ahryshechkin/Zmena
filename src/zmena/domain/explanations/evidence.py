from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from zmena.domain.model.hypothesis import Hypothesis


@dataclass
class Evidence:
    hypothesis: Hypothesis
    signal: float
    confidence: float
    reason: str

    def __repr__(self):
        return f"Evidence(signal={self.signal},confidence={self.confidence},reason={self.reason})"

    def score(self):
        return self.signal * self.confidence
