import unittest

from zmena.application import AnalysisPipeline, SQLIntakePipeline
from zmena.infrastructure import ScenarioCatalog


class TestSQLIntakeScenarios(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.catalog = ScenarioCatalog()

    def normalize(self, link):
        return str(link).split("|", 1)[1]

    def collect_winners(self, scenario):
        sqli = SQLIntakePipeline(scenario.before, scenario.after)
        before, after = sqli.run()

        sme = AnalysisPipeline(before, after)
        result = sme.run()

        winners = []
        for decision in result.decisions:
            winners.extend([self.normalize(link) for link in decision.winners()])

        return winners

    def test_sce_701_add_column_neat_before_neat_after(self):
        scenario = self.catalog.get("771")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(actual, scenario.expected)
