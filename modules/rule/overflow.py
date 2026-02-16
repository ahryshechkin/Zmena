from modules.constant import RuleId
from modules.model import Link

from .base import Rule


class RuleOverflow(Rule):
    def __init__(self):
        super().__init__(RuleId.OVERFLOW)


    def apply(self, scopes):
        return []
