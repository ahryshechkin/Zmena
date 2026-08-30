from enum import StrEnum


class StatementKind(StrEnum):
    ADD_COLUMN = "add column"
    ALTER_DATA_TYPE = "alter data type"
    DROP_COLUMN = "drop column"
    DROP_NOT_NULL = "drop not null"
    RENAME_COLUMN = "rename column"
    SET_NOT_NULL = "set not null"
