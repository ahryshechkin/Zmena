import unittest

from application import Pipeline, ScenarioCatalog


class TestBasicScenarios(unittest.TestCase):
    def setUp(self):
        self.catalog = ScenarioCatalog()


    def test_sce_014_alter_constraint_null(self):
        scenario = self.catalog.scenario("014")
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for links in result["selected_links"]:
            actual.extend([str(link) for link in links])

        self.assertCountEqual(actual, scenario.expected)
