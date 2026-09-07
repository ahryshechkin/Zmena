from enum import StrEnum


class SnapshotKind(StrEnum):
    MATCH = "match"
    STATE = "state"
    UNDEFINED = "undefined"
