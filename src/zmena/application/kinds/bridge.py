from enum import StrEnum


class BridgeKind(StrEnum):
    COMPONENT = "component"
    DECISION = "decision"
    FRAGMENT = "fragment"
    MATCH_BUNDLE = "match bundle"
    LINK = "link"
    STATE = "state"
    UNDEFINED = "undefined"
