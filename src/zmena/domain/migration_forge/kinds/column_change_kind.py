from enum import StrEnum


class ColumnChangeKind(StrEnum):
    ADD = "add"
    DROP = "drop"
    MODIFY = "modify"
    UNCHANGED = "unchanged"
