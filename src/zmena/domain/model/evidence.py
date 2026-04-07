from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from zmena.domain.model.hypothesis import Hypothesis


@dataclass
class Evidence:
    hypothesis: Hypothesis
    score: int
    reason: str
