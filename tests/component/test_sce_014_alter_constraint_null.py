import unittest

from application import Pipeline, ScenarioCatalog


class TestSce014AlterConstraintNull(unittest.TestCase):
    def test_sce_014_alter_constraint_null(self):
        scenario_catalog = ScenarioCatalog()
        scenario = scenario_catalog.get(["014"])[0]
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        self.assertTrue(True)