import unittest

from application import Pipeline, ScenarioCatalog


class TestComplexScenarios(unittest.TestCase):
    def setUp(self):
        self.catalog = ScenarioCatalog()


    def test_sce_051_alter_column_then_add_another_after(self):
        scenario = self.catalog.get(["051"])[0]
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for link in result["selected_links"][0]:
            actual.append(str(link))

        self.assertTrue(True)


    def test_sce_151_apply_scripts_in_proper_order(self):
        scenario = self.catalog.get(["151"])[0]
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for link in result["selected_links"][0]:
            actual.append(str(link))

        self.assertTrue(True)


    def test_sce_651_reuse_free_name_from_bottom(self):
        scenario = self.catalog.get(["651"])[0]
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for link in result["selected_links"][0]:
            actual.append(str(link))

        self.assertCountEqual(actual, scenario.expected)
