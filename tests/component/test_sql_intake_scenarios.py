import unittest

from zmena.application.messages.sql_intake import SQLIntakeMessage
from zmena.application.semantic_engine_pipeline import SemanticEnginePipeline
from zmena.application.sql_intake_pipeline import SQLIntakePipeline
from zmena.infrastructure.adapters.scenario_catalog import ScenarioCatalog


class TestSQLIntakeScenarios(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.catalog = ScenarioCatalog()

    def normalize(self, link):
        return str(link).split("|", 1)[1]

    def collect_winners(self, scenario):
        message = SQLIntakeMessage("", scenario.before, scenario.after)
        pipeline = SQLIntakePipeline(message)
        before, after = pipeline.run()

        pipeline = SemanticEnginePipeline(before, after)
        result = pipeline.run()

        winners = []
        for decision in result.decisions:
            winners.extend([self.normalize(link) for link in decision.winners()])

        return winners

    def test_sce_701_add_column_neat_before_neat_after(self):
        scenario = self.catalog.get("701")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_702_add_column_neat_before_chaotic_after(self):
        scenario = self.catalog.get("702")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_703_add_column_chaotic_before_neat_after(self):
        scenario = self.catalog.get("703")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_704_add_column_single_line_table(self):
        scenario = self.catalog.get("704")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_705_add_column_neat_before_uppercase_after(self):
        scenario = self.catalog.get("705")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_706_add_column_neat_before_lowercase_after(self):
        scenario = self.catalog.get("706")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_707_add_column_neat_before_mixed_after(self):
        scenario = self.catalog.get("707")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_708_add_column_blank_lines(self):
        scenario = self.catalog.get("708")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)

    def test_sce_709_rename_column_single_column_table(self):
        scenario = self.catalog.get("709")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(scenario.expected, actual)
