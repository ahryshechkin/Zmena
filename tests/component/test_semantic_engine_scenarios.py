import unittest

from zmena.application.messages.semantic_engine import SemanticEngineMessage
from zmena.application.semantic_engine_pipeline import SemanticEnginePipeline
from zmena.infrastructure.adapters.scenario_catalog import ScenarioCatalog


class TestSemanticEngineScenarios(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.catalog = ScenarioCatalog()

    def normalize(self, link):
        return str(link).split("|", 1)[1]

    def collect_winners(self, scenario):
        message = SemanticEngineMessage(scenario.before.splitlines(), scenario.after.splitlines())

        pipeline = SemanticEnginePipeline(message)
        result = pipeline.run()

        winners = []
        for decision in result.decisions:
            winners.extend([self.normalize(link) for link in decision.winners()])

        return winners

    def test_sce_011_add_column_not_null(self):
        scenario = self.catalog.get("011")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_012_add_column_null(self):
        scenario = self.catalog.get("012")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_013_alter_constraint_not_null(self):
        scenario = self.catalog.get("013")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_014_alter_constraint_null(self):
        scenario = self.catalog.get("014")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_015_change_data_type(self):
        scenario = self.catalog.get("015")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_016_drop_column(self):
        scenario = self.catalog.get("016")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_017_move_column(self):
        scenario = self.catalog.get("017")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_018_rename_column(self):
        scenario = self.catalog.get("018")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_019_rename_column_then_change_data_type(self):
        scenario = self.catalog.get("019")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_020_rename_column_then_alter_constraint(self):
        scenario = self.catalog.get("020")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_041_apply_multiple_primitive_changes(self):
        scenario = self.catalog.get("041")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_051_alter_column_then_add_another_before(self):
        scenario = self.catalog.get("051")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_052_alter_column_then_add_another_after(self):
        scenario = self.catalog.get("052")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_053_alter_column_then_drop_another_before(self):
        scenario = self.catalog.get("053")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_054_alter_column_then_drop_another_after(self):
        scenario = self.catalog.get("054")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_061_alter_column_then_rename_two_adjacent_ones(self):
        scenario = self.catalog.get("061")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_071_apply_changes_in_correct_order(self):
        scenario = self.catalog.get("071")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_201_swap_columns(self):
        scenario = self.catalog.get("201")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_202_swap_columns_nested(self):
        scenario = self.catalog.get("202")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_203_swap_columns_with_overlap(self):
        scenario = self.catalog.get("203")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_204_swap_adjacent_columns_with_same_signature(self):
        scenario = self.catalog.get("204")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_205_swap_close_columns_with_same_signature(self):
        scenario = self.catalog.get("205")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_206_swap_distant_columns_with_same_signature(self):
        scenario = self.catalog.get("206")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_207_add_column_between_adjacent_swapped_ones(self):
        scenario = self.catalog.get("207")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_208_add_column_between_non_adjacent_swapped_ones(self):
        scenario = self.catalog.get("208")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_221_move_three_columns_in_cycle(self):
        scenario = self.catalog.get("221")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_301_move_column_before_single_signature_alter(self):
        scenario = self.catalog.get("301")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_302_move_column_after_single_signature_alter(self):
        scenario = self.catalog.get("302")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_303_move_column_before_single_constraint_alter(self):
        scenario = self.catalog.get("303")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_304_move_column_before_single_type_alter(self):
        scenario = self.catalog.get("304")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_311_move_column_before_two_signature_alter(self):
        scenario = self.catalog.get("311")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_312_move_column_after_two_signature_alter(self):
        scenario = self.catalog.get("312")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_313_move_column_before_two_constraint_alter(self):
        scenario = self.catalog.get("313")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_314_move_column_before_two_type_alter(self):
        scenario = self.catalog.get("314")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_401_move_two_columns_before_altered_one(self):
        scenario = self.catalog.get("401")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_402_move_two_columns_after_altered_one(self):
        scenario = self.catalog.get("402")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_403_move_two_columns_before_altered_one_twice(self):
        scenario = self.catalog.get("403")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_601_rename_column_then_move_another_before_from_top(self):
        scenario = self.catalog.get("601")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_602_rename_column_then_move_another_before_from_bottom(self):
        scenario = self.catalog.get("602")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_603_rename_column_then_move_another_after_from_top(self):
        scenario = self.catalog.get("603")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_604_rename_column_then_move_another_after_from_bottom(self):
        scenario = self.catalog.get("604")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_651_drop_column_then_reuse_free_name_from_top(self):
        scenario = self.catalog.get("651")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_652_drop_column_then_reuse_free_name_from_bottom(self):
        scenario = self.catalog.get("652")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_653_rename_column_then_take_released_name_from_top(self):
        scenario = self.catalog.get("653")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_654_rename_column_then_take_released_name_from_bottom(self):
        scenario = self.catalog.get("654")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)
