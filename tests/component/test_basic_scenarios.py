import unittest

from application import Pipeline, ScenarioCatalog


class TestBasicScenarios(unittest.TestCase):
    def setUp(self):
        self.catalog = ScenarioCatalog()


    def test_sce_014_alter_constraint_null(self):
        scenario = self.catalog.get(["014"])[0]
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for link in result["selected_links"][0]:
            actual.append(str(link))

        self.assertCountEqual(actual, scenario.expected)
