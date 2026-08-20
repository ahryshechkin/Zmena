from enum import StrEnum


class CriterionKind(StrEnum):
    EXCLUDED_EXTENSIONS = "excluded extensions"
    EXCLUDED_DIRECTORIES = "excluded directories"
    INCLUDED_EXTENSIONS = "included extensions"
    INCLUDED_DIRECTORIES = "included directories"
