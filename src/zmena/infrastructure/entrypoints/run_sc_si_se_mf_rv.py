from zmena.application.handoffs.migration_forge.from_sql_intake import (
    SQLIntakeToMigrationForgeHandoff,
)
from zmena.application.handoffs.release_vault.from_sql_intake import (
    SQLIntakeToReleaseVaultHandoff,
)
from zmena.application.handoffs.semantic_engine.from_sql_intake import (
    SQLIntakeToSemanticEngineHandoff,
)
from zmena.application.handoffs.sql_intake.from_scenario_catalog import (
    ScenarioCatalogToSQLIntakeHandoff,
)
from zmena.application.pipelines.migration_forge import MigrationForgePipeline
from zmena.application.pipelines.semantic_engine import SemanticEnginePipeline
from zmena.application.pipelines.sql_intake import SQLIntakePipeline
from zmena.domain.migration_forge.dialects.postgresql import PostgreSQLDialect
from zmena.infrastructure.adapters.catalogs.scenario import ScenarioCatalog
from zmena.infrastructure.adapters.release_vault import ReleaseVault
from zmena.infrastructure.release_batch import PartitionPath

sce_ids = ["702", "703"]
dialect = PostgreSQLDialect()
path = PartitionPath()
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    handoff = ScenarioCatalogToSQLIntakeHandoff(scenario)
    sii_message = handoff.prepare()

    pipeline = SQLIntakePipeline(sii_message)
    sio_message = pipeline.run()

    handoff = SQLIntakeToSemanticEngineHandoff(sio_message)
    sei_message = handoff.prepare()

    pipeline = SemanticEnginePipeline(sei_message)
    seo_message = pipeline.run()

    handoff = SQLIntakeToMigrationForgeHandoff(dialect, sio_message, seo_message)
    mfi_message = handoff.prepare()

    pipeline = MigrationForgePipeline(mfi_message)
    mfo_message = pipeline.run()

    handoff = SQLIntakeToReleaseVaultHandoff(path.generate(), sio_message, mfo_message)
    rvi_message = handoff.prepare()

    vault = ReleaseVault(rvi_message)
    vault.save()
