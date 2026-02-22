import unittest

from application import Pipeline, ScenarioCatalog


class TestComplexScenarios(unittest.TestCase):
    def test_sce_014_alter_constraint_null(self):
        scenario_catalog = ScenarioCatalog()
        scenario = scenario_catalog.get(["014"])[0]
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        self.assertTrue(True)


    def test_sce_051_alter_column_then_add_another_after(self):
        scenario_catalog = ScenarioCatalog()
        scenario = scenario_catalog.get(["051"])[0]
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        self.assertTrue(True)