import unittest

from zmena.application.messages.inbound.migration_forge import MigrationForgeInboundMessage
from zmena.application.messages.inbound.semantic_engine import SemanticEngineInboundMessage
from zmena.application.pipelines.migration_forge import MigrationForgePipeline
from zmena.application.pipelines.semantic_engine import SemanticEnginePipeline
from zmena.domain.migration_forge.snapshots.state import Snapshot
from zmena.infrastructure.adapters.catalogs.mf_fixture import MFFixtureCatalog
from zmena.infrastructure.adapters.catalogs.scenario import ScenarioCatalog


class TestSemanticEngineScenarios(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.sce_catalog = ScenarioCatalog()
        self.fix_catalog = MFFixtureCatalog()

    def test_sce_011_add_column_not_null(self):
        scenario = self.sce_catalog.get("011")
        expected = self.fix_catalog.get("011")

        sei_message = SemanticEngineInboundMessage(
            before=scenario.before.splitlines(), after=scenario.after.splitlines()
        )
        pipeline = SemanticEnginePipeline(sei_message)
        seo_message = pipeline.run()

        _, right = seo_message.decisions[0].winners()[0].fragments()
        before = None
        after = Snapshot(
            name=right.name, data_type=right.data_type, nullable=right.constraint != "NOT NULL"
        )
        message = MigrationForgeInboundMessage(before=before, after=after)

        pipeline = MigrationForgePipeline(message)
        actual = pipeline.run()

        self.assertCountEqual(expected, actual)
