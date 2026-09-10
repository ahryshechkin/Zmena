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

    def test_sce_012_add_column_null(self):
        scenario = self.sce_catalog.get("012")
        expected = self.fix_catalog.get("012")
        actual = self.execute_pipeline(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_013_set_not_null(self):
        scenario = self.sce_catalog.get("013")
        expected = self.fix_catalog.get("013")
        actual = self.execute_pipeline(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_014_drop_not_null(self):
        scenario = self.sce_catalog.get("014")
        expected = self.fix_catalog.get("014")
        actual = self.execute_pipeline(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_015_alter_data_type(self):
        scenario = self.sce_catalog.get("015")
        expected = self.fix_catalog.get("015")
        actual = self.execute_pipeline(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_016_drop_column(self):
        scenario = self.sce_catalog.get("016")
        expected = self.fix_catalog.get("016")
        actual = self.execute_pipeline(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_017_move_column(self):
        scenario = self.sce_catalog.get("017")
        expected = self.fix_catalog.get("017")
        actual = self.execute_pipeline(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_018_rename_column(self):
        scenario = self.sce_catalog.get("018")
        expected = self.fix_catalog.get("018")
        actual = self.execute_pipeline(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_019_rename_column_then_alter_data_type(self):
        scenario = self.sce_catalog.get("019")
        expected = self.fix_catalog.get("019")
        actual = self.execute_pipeline(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_020_rename_column_then_drop_not_null(self):
        scenario = self.sce_catalog.get("020")
        expected = self.fix_catalog.get("020")
        actual = self.execute_pipeline(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_041_apply_multiple_primitive_changes(self):
        scenario = self.sce_catalog.get("041")
        expected = self.fix_catalog.get("041")
        actual = self.execute_pipeline(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_051_alter_column_then_add_another_before(self):
        scenario = self.sce_catalog.get("051")
        expected = self.fix_catalog.get("051")
        actual = self.execute_pipeline(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_052_alter_column_then_add_another_after(self):
        scenario = self.sce_catalog.get("052")
        expected = self.fix_catalog.get("052")
        actual = self.execute_pipeline(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_053_alter_column_then_drop_another_before(self):
        scenario = self.sce_catalog.get("053")
        expected = self.fix_catalog.get("053")
        actual = self.execute_pipeline(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_054_alter_column_then_drop_another_after(self):
        scenario = self.sce_catalog.get("054")
        expected = self.fix_catalog.get("054")
        actual = self.execute_pipeline(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_061_alter_column_then_rename_two_adjacent_ones(self):
        scenario = self.sce_catalog.get("061")
        expected = self.fix_catalog.get("061")
        actual = self.execute_pipeline(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_071_apply_changes_in_correct_order(self):
        scenario = self.sce_catalog.get("071")
        expected = self.fix_catalog.get("071")
        actual = self.execute_pipeline(scenario)

        self.assertCountEqual(expected, actual)
