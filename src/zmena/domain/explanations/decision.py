from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from zmena.domain.explanations.link import ExplanationLink


@dataclass
class ExplanationDecision:
    links: list[ExplanationLink]
