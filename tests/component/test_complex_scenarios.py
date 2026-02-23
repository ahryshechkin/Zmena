import unittest

from application import Pipeline, ScenarioCatalog


class TestComplexScenarios(unittest.TestCase):
    def setUp(self):
        self.catalog = ScenarioCatalog()


    def test_sce_051_alter_column_then_add_another_after(self):
        scenario = self.catalog.scenario("051")
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for links in result["selected_links"]:
            actual.extend([str(link) for link in links])

        self.assertCountEqual(actual, scenario.expected)


    def test_sce_151_apply_scripts_in_proper_order(self):
        scenario = self.catalog.scenario("151")
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for links in result["selected_links"]:
            actual.extend([str(link) for link in links])

        self.assertCountEqual(actual, scenario.expected)


    def test_sce_651_reuse_free_name_from_bottom(self):
        scenario = self.catalog.scenario("651")
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for links in result["selected_links"]:
            actual.extend([str(link) for link in links])

        self.assertCountEqual(actual, scenario.expected)
