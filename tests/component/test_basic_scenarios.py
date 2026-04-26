import unittest

from zmena.application import AnalysisPipeline, ScenarioCatalog


class TestBasicScenarios(unittest.TestCase):
    def setUp(self):
        self.catalog = ScenarioCatalog()

    def test_sce_011_add_column_not_null(self):
        scenario = self.catalog.get("011")
        pipeline = AnalysisPipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = []
        for decision in result["decisions"]:
            actual.extend([str(link) for link in decision.chosen()])

        self.assertCountEqual(actual, scenario.expected)

    def test_sce_012_add_column_null(self):
        scenario = self.catalog.get("012")
        pipeline = AnalysisPipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = []
        for decision in result["decisions"]:
            actual.extend([str(link) for link in decision.chosen()])

        self.assertCountEqual(actual, scenario.expected)

    def test_sce_013_alter_constraint_not_null(self):
        scenario = self.catalog.get("013")
        pipeline = AnalysisPipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = []
        for decision in result["decisions"]:
            actual.extend([str(link) for link in decision.chosen()])

        self.assertCountEqual(actual, scenario.expected)

    def test_sce_014_alter_constraint_null(self):
        scenario = self.catalog.get("014")
        pipeline = AnalysisPipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = []
        for decision in result["decisions"]:
            actual.extend([str(link) for link in decision.chosen()])

        self.assertCountEqual(actual, scenario.expected)

    def test_sce_015_change_data_type(self):
        scenario = self.catalog.get("015")
        pipeline = AnalysisPipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = []
        for decision in result["decisions"]:
            actual.extend([str(link) for link in decision.chosen()])

        self.assertCountEqual(actual, scenario.expected)

    def test_sce_016_drop_column(self):
        scenario = self.catalog.get("016")
        pipeline = AnalysisPipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = []
        for decision in result["decisions"]:
            actual.extend([str(link) for link in decision.chosen()])

        self.assertCountEqual(actual, scenario.expected)

    def test_sce_017_move_column(self):
        scenario = self.catalog.get("017")
        pipeline = AnalysisPipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = []
        for decision in result["decisions"]:
            actual.extend([str(link) for link in decision.chosen()])

        self.assertCountEqual(actual, scenario.expected)
