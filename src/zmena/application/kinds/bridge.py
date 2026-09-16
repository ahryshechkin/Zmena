from enum import StrEnum


class BridgeKind(StrEnum):
    COMPONENT = "component"
    DECISION = "decision"
    FRAGMENT = "fragment"
    MATCH_BUNDLE = "match bundle"
    LIGHTWEIGHT_LINK = "lightweight link"
    LINK = "link"
    STATE = "state"
    UNDEFINED = "undefined"
