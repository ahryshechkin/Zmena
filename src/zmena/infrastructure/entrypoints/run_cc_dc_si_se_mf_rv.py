from zmena.application.handoffs.delta_crawler.from_commit_catalog import (
    CommitCatalogToDeltaCrawlerHandoff,
)
from zmena.application.handoffs.migration_forge.from_sql_intake import (
    SQLIntakeToMigrationForgeHandoff,
)
from zmena.application.handoffs.release_vault.from_sql_intake import (
    SQLIntakeToReleaseVaultHandoff,
)
from zmena.application.handoffs.semantic_engine.from_sql_intake import (
    SQLIntakeToSemanticEngineHandoff,
)
from zmena.application.handoffs.sql_intake.from_delta_crawler import (
    DeltaCrawlerToSQLIntakeHandoff,
)
from zmena.application.pipelines.delta_crawler import DeltaCrawlerPipeline
from zmena.application.pipelines.migration_forge import MigrationForgePipeline
from zmena.application.pipelines.semantic_engine import SemanticEnginePipeline
from zmena.application.pipelines.sql_intake import SQLIntakePipeline
from zmena.domain.migration_forge.dialects.postgresql import PostgreSQLDialect
from zmena.infrastructure.adapters.catalogs.commit import CommitCatalog
from zmena.infrastructure.adapters.release_vault import ReleaseVault
from zmena.infrastructure.release_batch import ReleaseBatch

dialect = PostgreSQLDialect()
release_batch = ReleaseBatch()
catalog = CommitCatalog()
# catalog.cleanup_demo_repo()
# catalog.build_demo_repo()

handoff = CommitCatalogToDeltaCrawlerHandoff("v0.1.008", "v0.1.009", dialect, release_batch)
dci_message = handoff.prepare()

pipeline = DeltaCrawlerPipeline(dci_message)
for dco_message in pipeline.run():
    handoff = DeltaCrawlerToSQLIntakeHandoff(dco_message)
    sii_message = handoff.prepare()

    pipeline = SQLIntakePipeline(sii_message)
    sio_message = pipeline.run()

    handoff = SQLIntakeToSemanticEngineHandoff(sio_message)
    sei_message = handoff.prepare()

    pipeline = SemanticEnginePipeline(sei_message)
    seo_message = pipeline.run()

    handoff = SQLIntakeToMigrationForgeHandoff(sio_message, seo_message)
    mfi_message = handoff.prepare()

    pipeline = MigrationForgePipeline(mfi_message)
    mfo_message = pipeline.run()

    handoff = SQLIntakeToReleaseVaultHandoff(sio_message, mfo_message)
    rvi_message = handoff.prepare()

    vault = ReleaseVault(rvi_message)
    vault.save_migrations()
