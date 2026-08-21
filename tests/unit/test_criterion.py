import unittest

from zmena.domain.delta_crawler.criteria.criterion import Criterion
from zmena.domain.delta_crawler.criteria.excluded_directories import ExcludedDirectoriesCriterion
from zmena.domain.delta_crawler.kinds.criterion_kind import CriterionKind


class TestCriterion(unittest.TestCase):
    def test_repr(self):
        criterion = Criterion(CriterionKind.EXCLUDED_DIRECTORIES)
        self.assertEqual("Criterion(kind=excluded directories)", repr(criterion))


class TestExcludedDirectoriesCriterion(unittest.TestCase):
    def setUp(self):
        self.samples = [
            "code/scripts/script.py",
            "code/scripts/sql.txt",
            "code/scripts/sql.sql",
            "code/sql/scripts/script.py",
            "infra/catalog/schema/tab.sql",
            "infra/catalog/sql/tab.sql",
            "infra/catalog/sql/script.py",
            "infra/catalog/sql.py",
            "sql.sql",
            "text.sql",
            "text.txt",
        ]

    def test_apply_empty_filter(self):
        expected = self.samples
        criterion = ExcludedDirectoriesCriterion([])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_full_path(self):
        expected = [
            "code/scripts/script.py",
            "code/scripts/sql.txt",
            "code/scripts/sql.sql",
            "code/sql/scripts/script.py",
            "infra/catalog/schema/tab.sql",
            "infra/catalog/sql.py",
            "sql.sql",
            "text.sql",
            "text.txt",
        ]
        criterion = ExcludedDirectoriesCriterion(["infra/catalog/sql"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_partial_path(self):
        expected = [
            "code/scripts/script.py",
            "code/scripts/sql.txt",
            "code/scripts/sql.sql",
            "infra/catalog/schema/tab.sql",
            "infra/catalog/sql.py",
            "sql.sql",
            "text.txt",
            "text.sql",
        ]
        criterion = ExcludedDirectoriesCriterion(["sql"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)
