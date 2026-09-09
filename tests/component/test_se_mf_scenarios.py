import unittest

from zmena.application.bridges.match_bundle import MatchBundleBridge
from zmena.application.bridges.state import StateBridge
from zmena.application.messages.inbound.migration_forge import MigrationForgeInboundMessage
from zmena.application.messages.inbound.semantic_engine import SemanticEngineInboundMessage
from zmena.application.pipelines.migration_forge import MigrationForgePipeline
from zmena.application.pipelines.semantic_engine import SemanticEnginePipeline
from zmena.infrastructure.adapters.catalogs.mf_fixture import MFFixtureCatalog
from zmena.infrastructure.adapters.catalogs.scenario import ScenarioCatalog


class TestSemanticEngineScenarios(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.sce_catalog = ScenarioCatalog()
        self.fix_catalog = MFFixtureCatalog()

    def execute_pipeline(self, scenario):
        sei_message = SemanticEngineInboundMessage(
            before=scenario.before.splitlines(), after=scenario.after.splitlines()
        )
        pipeline = SemanticEnginePipeline(sei_message)
        seo_message = pipeline.run()

        bridge = MatchBundleBridge(StateBridge())
        matches = bridge.translate(seo_message.decisions_new)

        mfi_message = MigrationForgeInboundMessage(matches=matches)
        pipeline = MigrationForgePipeline(mfi_message)
        mfo_message = pipeline.run()

        return mfo_message.statements

    def test_sce_011_add_column_not_null(self):
        scenario = self.sce_catalog.get("011")
        expected = self.fix_catalog.get("011")
        actual = self.execute_pipeline(scenario)

        self.assertCountEqual(expected, actual)
