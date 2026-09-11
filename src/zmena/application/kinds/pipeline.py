from enum import StrEnum


class PipelineKind(StrEnum):
    DELTA_CRAWLER = "delta crawler"
    MIGRATION_FORGE = "migration forge"
    SEMANTIC_ENGINE = "semantic engine"
    SQL_INTAKE = "sql intake"
    UNDEFINED = "undefined"
