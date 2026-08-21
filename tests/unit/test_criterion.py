import unittest

from zmena.domain.delta_crawler.criteria.criterion import Criterion
from zmena.domain.delta_crawler.criteria.excluded_directories import ExcludedDirectoriesCriterion
from zmena.domain.delta_crawler.kinds.criterion_kind import CriterionKind


class TestCriterion(unittest.TestCase):
    def test_repr(self):
        criterion = Criterion(CriterionKind.EXCLUDED_DIRECTORIES)
        self.assertEqual("Criterion(kind=excluded directories)", repr(criterion))


class TestExcludedDirectoriesCriterion(unittest.TestCase):
    def test_apply(self):
        criterion = ExcludedDirectoriesCriterion([""])

        expected = []
        actual = criterion.apply(
            [
                "code/scripts/script01.py",
                "code/scripts/sql.txt",
                "code/domain/sql.sql",
                "infra/catalog/schema/tab01.sql",
                "infra/catalog/sql/tab02.sql",
                "infra/catalog/sql/script02.py",
                "text01.txt",
                "text02.sql",
            ]
        )

        self.assertCountEqual(expected, actual)
