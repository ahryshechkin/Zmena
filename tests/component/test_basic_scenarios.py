import unittest

from application import Pipeline, ScenarioCatalog


class TestBasicScenarios(unittest.TestCase):
    def setUp(self):
        self.catalog = ScenarioCatalog()


    def test_sce_011_add_column_not_null(self):
        scenario = self.catalog.scenario("011")
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for links in result["selected_links"]:
            actual.extend([str(link) for link in links])

        self.assertCountEqual(actual, scenario.expected)


    def test_sce_012_add_column_null(self):
        scenario = self.catalog.scenario("012")
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for links in result["selected_links"]:
            actual.extend([str(link) for link in links])

        self.assertCountEqual(actual, scenario.expected)


    def test_sce_013_alter_constraint_not_null(self):
        scenario = self.catalog.scenario("013")
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for links in result["selected_links"]:
            actual.extend([str(link) for link in links])

        self.assertCountEqual(actual, scenario.expected)


    def test_sce_014_alter_constraint_null(self):
        scenario = self.catalog.scenario("014")
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for links in result["selected_links"]:
            actual.extend([str(link) for link in links])

        self.assertCountEqual(actual, scenario.expected)


    def test_sce_015_change_data_type(self):
        scenario = self.catalog.scenario("015")
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for links in result["selected_links"]:
            actual.extend([str(link) for link in links])

        self.assertCountEqual(actual, scenario.expected)


    def test_sce_016_drop_column(self):
        scenario = self.catalog.scenario("016")
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for links in result["selected_links"]:
            actual.extend([str(link) for link in links])

        self.assertCountEqual(actual, scenario.expected)


    def test_sce_017_move_column(self):
        scenario = self.catalog.scenario("017")
        pipeline = Pipeline(scenario.before, scenario.after)
        result = pipeline.run()

        actual = list()
        for links in result["selected_links"]:
            actual.extend([str(link) for link in links])

        self.assertCountEqual(actual, scenario.expected)
