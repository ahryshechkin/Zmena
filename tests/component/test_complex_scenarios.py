import unittest

from application import Pipeline, ScenarioCatalog


class TestComplexScenarios(unittest.TestCase):
    def setUp(self):
        self.catalog = ScenarioCatalog()


    def test_sce_051_alter_column_then_add_another_before(self):
        scenario = self.catalog.scenario("051")
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for links in result["selected_links"]:
            actual.extend([str(link) for link in links])

        self.assertCountEqual(actual, scenario.expected)


    def test_sce_052_alter_column_then_add_another_after(self):
        scenario = self.catalog.scenario("052")
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for links in result["selected_links"]:
            actual.extend([str(link) for link in links])

        self.assertCountEqual(actual, scenario.expected)


    def test_sce_053_alter_column_then_rename_two_adjacent_ones(self):
        scenario = self.catalog.scenario("053")
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


    def test_sce_301_move_column_before_single_signature_alter(self):
        scenario = self.catalog.scenario("301")
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for links in result["selected_links"]:
            actual.extend([str(link) for link in links])

        self.assertCountEqual(actual, scenario.expected)


    def test_sce_302_move_column_after_single_signature_alter(self):
        scenario = self.catalog.scenario("302")
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for links in result["selected_links"]:
            actual.extend([str(link) for link in links])

        self.assertCountEqual(actual, scenario.expected)


    def test_sce_303_move_column_before_single_constraint_alter(self):
        scenario = self.catalog.scenario("303")
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for links in result["selected_links"]:
            actual.extend([str(link) for link in links])

        self.assertCountEqual(actual, scenario.expected)


    def test_sce_304_move_column_before_single_type_alter(self):
        scenario = self.catalog.scenario("304")
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for links in result["selected_links"]:
            actual.extend([str(link) for link in links])

        self.assertCountEqual(actual, scenario.expected)


    def test_sce_311_move_column_before_two_signature_alter(self):
        scenario = self.catalog.scenario("311")
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for links in result["selected_links"]:
            actual.extend([str(link) for link in links])

        self.assertCountEqual(actual, scenario.expected)


    def test_sce_312_move_column_after_two_signature_alter(self):
        scenario = self.catalog.scenario("312")
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for links in result["selected_links"]:
            actual.extend([str(link) for link in links])

        self.assertCountEqual(actual, scenario.expected)


    def test_sce_313_move_column_before_two_constraint_alter(self):
        scenario = self.catalog.scenario("313")
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for links in result["selected_links"]:
            actual.extend([str(link) for link in links])

        self.assertCountEqual(actual, scenario.expected)


    def test_sce_314_move_column_before_two_type_alter(self):
        scenario = self.catalog.scenario("314")
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
