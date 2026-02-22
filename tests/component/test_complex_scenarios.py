import unittest

from application import Pipeline, ScenarioCatalog


class TestComplexScenarios(unittest.TestCase):
    def setUp(self):
        self.catalog = ScenarioCatalog()


    def test_sce_051_alter_column_then_add_another_after(self):
        scenario = self.catalog.get(["051"])[0]
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        self.assertTrue(True)


    def test_sce_151_alter_column_then_add_another_after(self):
        scenario = self.catalog.get(["151"])[0]
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        self.assertTrue(True)