import unittest

from zmena.domain.delta_crawler.criteria.excluded_directories import ExcludedDirectoriesCriterion
from zmena.domain.delta_crawler.kinds.criterion_kind import CriterionKind


class TestExcludedDirectionsCriterion(unittest.TestCase):
    def test_repr(self):
        criterion = ExcludedDirectoriesCriterion(CriterionKind.EXCLUDED_DIRECTORIES)
        self.assertEqual("Criterion(kind=excluded directories)", repr(criterion))
