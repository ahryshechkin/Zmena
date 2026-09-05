import unittest

from zmena.application.messages.inbound.semantic_engine import SemanticEngineInboundMessage
from zmena.application.messages.inbound.sql_intake import SQLIntakeInboundMessage
from zmena.application.pipelines.semantic_engine import SemanticEnginePipeline
from zmena.application.pipelines.sql_intake import SQLIntakePipeline
from zmena.infrastructure.adapters.catalogs.fixture_se import FixtureSECatalog
from zmena.infrastructure.adapters.catalogs.scenario import ScenarioCatalog


class TestSQLIntakeSemanticEngineScenarios(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.sce_catalog = ScenarioCatalog()
        self.fix_catalog = FixtureSECatalog()

    def normalize(self, link):
        return str(link).split("|", 1)[1]

    def collect_winners(self, scenario):
        sii_message = SQLIntakeInboundMessage(
            label=scenario.sce_id, name=scenario.name, before=scenario.before, after=scenario.after
        )
        pipeline = SQLIntakePipeline(sii_message)
        sio_message = pipeline.run()

        sei_message = SemanticEngineInboundMessage(
            before=sio_message.before, after=sio_message.after
        )
        pipeline = SemanticEnginePipeline(sei_message)
        seo_message = pipeline.run()

        winners = []
        for decision in seo_message.decisions:
            winners.extend([self.normalize(link) for link in decision.winners()])

        return winners

    def test_sce_701_add_column_neat_before_neat_after(self):
        scenario = self.sce_catalog.get("701")
        expected = self.fix_catalog.get("701")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_702_add_column_neat_before_chaotic_after(self):
        scenario = self.sce_catalog.get("702")
        expected = self.fix_catalog.get("702")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_703_add_column_chaotic_before_neat_after(self):
        scenario = self.sce_catalog.get("703")
        expected = self.fix_catalog.get("703")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_704_add_column_single_line_table(self):
        scenario = self.sce_catalog.get("704")
        expected = self.fix_catalog.get("704")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_705_add_column_neat_before_uppercase_after(self):
        scenario = self.sce_catalog.get("705")
        expected = self.fix_catalog.get("705")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_706_add_column_neat_before_lowercase_after(self):
        scenario = self.sce_catalog.get("706")
        expected = self.fix_catalog.get("706")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_707_add_column_neat_before_mixed_after(self):
        scenario = self.sce_catalog.get("707")
        expected = self.fix_catalog.get("707")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_708_add_column_blank_lines(self):
        scenario = self.sce_catalog.get("708")
        expected = self.fix_catalog.get("708")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(expected, actual)

    def test_sce_709_rename_column_single_column_table(self):
        scenario = self.sce_catalog.get("709")
        expected = self.fix_catalog.get("709")
        actual = self.collect_winners(scenario)

        self.assertCountEqual(expected, actual)
