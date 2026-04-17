from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from zmena.domain.model.brick.base import Brick
    from zmena.domain.model.evidence import Evidence


@dataclass
class ExplanationLink:
    bricks: tuple[Brick, Brick]
    score: int
    evidences: list[Evidence]
