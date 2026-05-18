import unittest

from zmena.application import AnalysisPipeline
from zmena.infrastructure import ScenarioCatalog


class TestBasicScenarios(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.catalog = ScenarioCatalog()

    def normalize(self, link):
        return str(link).split("|", 1)[1]

    def collect_winners(self, scenario):
        pipeline = AnalysisPipeline(scenario.before, scenario.after)
        result = pipeline.run()

        winners = []
        for decision in result.decisions:
            winners.extend([self.normalize(link) for link in decision.winners()])

        return winners

    def test_sce_011_add_column_not_null(self):
        scenario = self.catalog.get("011")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(actual, scenario.expected)

    def test_sce_012_add_column_null(self):
        scenario = self.catalog.get("012")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(actual, scenario.expected)

    def test_sce_013_alter_constraint_not_null(self):
        scenario = self.catalog.get("013")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(actual, scenario.expected)

    def test_sce_014_alter_constraint_null(self):
        scenario = self.catalog.get("014")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(actual, scenario.expected)

    def test_sce_015_change_data_type(self):
        scenario = self.catalog.get("015")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(actual, scenario.expected)

    def test_sce_016_drop_column(self):
        scenario = self.catalog.get("016")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(actual, scenario.expected)

    def test_sce_017_move_column(self):
        scenario = self.catalog.get("017")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(actual, scenario.expected)

    def test_sce_018_rename_column(self):
        scenario = self.catalog.get("018")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(actual, scenario.expected)

    def test_sce_019_rename_column_then_change_data_type(self):
        scenario = self.catalog.get("019")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(actual, scenario.expected)

    def test_sce_020_rename_column_then_alter_constraint(self):
        scenario = self.catalog.get("020")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(actual, scenario.expected)

    def test_sce_041_apply_multiple_primitive_changes(self):
        scenario = self.catalog.get("041")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(actual, scenario.expected)
