import unittest

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
        pipeline = SQLIntakePipeline(scenario.before, scenario.after)
        before, after = pipeline.run()

        pipeline = SemanticEnginePipeline(before, after)
        result = pipeline.run()

        winners = []
        for decision in result.decisions:
            winners.extend([self.normalize(link) for link in decision.winners()])

        return winners

    def test_sce_701_add_column_neat_before_neat_after(self):
        scenario = self.catalog.get("771")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(actual, scenario.expected)
