import unittest

from zmena.domain.delta_crawler.criteria.criterion import Criterion
from zmena.domain.delta_crawler.criteria.excluded_directories import ExcludedDirectoriesCriterion
from zmena.domain.delta_crawler.criteria.excluded_extensions import ExcludedExtensionsCriterion
from zmena.domain.delta_crawler.criteria.included_directories import IncludedDirectoriesCriterion
from zmena.domain.delta_crawler.kinds.criterion_kind import CriterionKind


class TestCriterion(unittest.TestCase):
    def test_repr(self):
        criterion = Criterion(CriterionKind.EXCLUDED_DIRECTORIES)
        self.assertEqual("Criterion(kind=excluded directories)", repr(criterion))


class TestExcludedDirectoriesCriterion(unittest.TestCase):
    def setUp(self):
        self.samples = [
            "code/scripts/script.py",
            "code/scripts/script.y",
            "code/scripts/sql.sql",
            "code/scripts/sql.txt",
            "code/sql/scripts/script.py",
            "infra/catalog/schema/tab.sql",
            "infra/catalog/sql.py",
            "infra/catalog/sql/script.py",
            "infra/catalog/sql/tab.sql",
            "infra\\catalog\\schema\\script.sql",
            "sql.sql",
            "text.sql",
            "text.txt",
        ]

    def test_apply_empty_filter(self):
        expected = self.samples
        criterion = ExcludedDirectoriesCriterion([])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_filter_with_backslash(self):
        expected = [
            "code/scripts/script.py",
            "code/scripts/script.y",
            "code/scripts/sql.sql",
            "code/scripts/sql.txt",
            "code/sql/scripts/script.py",
            "infra/catalog/sql.py",
            "infra/catalog/sql/script.py",
            "infra/catalog/sql/tab.sql",
            "sql.sql",
            "text.sql",
            "text.txt",
        ]
        criterion = ExcludedDirectoriesCriterion(["catalog\\schema"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_full_path(self):
        expected = [
            "code/scripts/script.py",
            "code/scripts/script.y",
            "code/scripts/sql.sql",
            "code/scripts/sql.txt",
            "code/sql/scripts/script.py",
            "infra/catalog/schema/tab.sql",
            "infra/catalog/sql.py",
            "infra\\catalog\\schema\\script.sql",
            "sql.sql",
            "text.sql",
            "text.txt",
        ]
        criterion = ExcludedDirectoriesCriterion(["infra/catalog/sql"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_leading_backslash(self):
        expected = [
            "code/scripts/script.py",
            "code/scripts/script.y",
            "code/scripts/sql.sql",
            "code/scripts/sql.txt",
            "code/sql/scripts/script.py",
            "sql.sql",
            "text.sql",
            "text.txt",
        ]
        criterion = ExcludedDirectoriesCriterion(["\\infra"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_leading_slash(self):
        expected = [
            "infra/catalog/schema/tab.sql",
            "infra/catalog/sql.py",
            "infra/catalog/sql/script.py",
            "infra/catalog/sql/tab.sql",
            "infra\\catalog\\schema\\script.sql",
            "sql.sql",
            "text.sql",
            "text.txt",
        ]
        criterion = ExcludedDirectoriesCriterion(["/code"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_partial_path(self):
        expected = [
            "code/scripts/script.py",
            "code/scripts/script.y",
            "code/scripts/sql.sql",
            "code/scripts/sql.txt",
            "infra/catalog/schema/tab.sql",
            "infra/catalog/sql.py",
            "infra\\catalog\\schema\\script.sql",
            "sql.sql",
            "text.sql",
            "text.txt",
        ]
        criterion = ExcludedDirectoriesCriterion(["sql"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_several_filters(self):
        expected = [
            "code/scripts/script.py",
            "code/scripts/script.y",
            "code/scripts/sql.sql",
            "code/scripts/sql.txt",
            "infra/catalog/schema/tab.sql",
            "infra/catalog/sql.py",
            "infra\\catalog\\schema\\script.sql",
            "sql.sql",
            "text.sql",
            "text.txt",
        ]
        criterion = ExcludedDirectoriesCriterion(["catalog/sql", "sql\\"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_trailing_backslash(self):
        expected = [
            "code/scripts/script.py",
            "code/scripts/script.y",
            "code/scripts/sql.sql",
            "code/scripts/sql.txt",
            "code/sql/scripts/script.py",
            "infra/catalog/sql.py",
            "infra/catalog/sql/script.py",
            "infra/catalog/sql/tab.sql",
            "sql.sql",
            "text.sql",
            "text.txt",
        ]
        criterion = ExcludedDirectoriesCriterion(["schema/"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_trailing_slash(self):
        expected = [
            "code/scripts/script.py",
            "code/scripts/script.y",
            "code/scripts/sql.sql",
            "code/scripts/sql.txt",
            "code/sql/scripts/script.py",
            "infra/catalog/sql.py",
            "infra/catalog/sql/script.py",
            "infra/catalog/sql/tab.sql",
            "sql.sql",
            "text.sql",
            "text.txt",
        ]
        criterion = ExcludedDirectoriesCriterion(["schema\\"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)


class TestExcludedExtensionsCriterion(unittest.TestCase):
    def setUp(self):
        self.samples = [
            "code/scripts/script.py",
            "code/scripts/script.y",
            "code/scripts/sql.sql",
            "code/scripts/sql.txt",
            "code/sql/scripts/script.py",
            "infra/catalog/schema/tab.sql",
            "infra/catalog/sql.py",
            "infra/catalog/sql/script.py",
            "infra/catalog/sql/tab.sql",
            "infra\\catalog\\schema\\script.sql",
            "sql.sql",
            "text.sql",
            "text.txt",
        ]

    def test_apply_empty_filter(self):
        expected = self.samples
        criterion = ExcludedExtensionsCriterion([])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_partial_extension(self):
        expected = [
            "code/scripts/script.py",
            "code/scripts/sql.sql",
            "code/scripts/sql.txt",
            "code/sql/scripts/script.py",
            "infra/catalog/schema/tab.sql",
            "infra/catalog/sql.py",
            "infra/catalog/sql/script.py",
            "infra/catalog/sql/tab.sql",
            "infra\\catalog\\schema\\script.sql",
            "sql.sql",
            "text.sql",
            "text.txt",
        ]
        criterion = ExcludedExtensionsCriterion(["y"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_several_extensions(self):
        expected = [
            "code/scripts/script.py",
            "code/scripts/script.y",
            "code/scripts/sql.txt",
            "code/sql/scripts/script.py",
            "infra/catalog/sql.py",
            "infra/catalog/sql/script.py",
            "text.txt",
        ]
        criterion = ExcludedExtensionsCriterion([".sql"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_single_extension(self):
        expected = [
            "code/scripts/script.y",
            "code/scripts/sql.sql",
            "infra/catalog/schema/tab.sql",
            "infra/catalog/sql/tab.sql",
            "infra\\catalog\\schema\\script.sql",
            "sql.sql",
            "text.sql",
        ]
        criterion = ExcludedExtensionsCriterion([".py", ".txt"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_suffix_only(self):
        expected = [
            "code/scripts/script.py",
            "code/scripts/script.y",
            "code/scripts/sql.txt",
            "code/sql/scripts/script.py",
            "infra/catalog/sql.py",
            "infra/catalog/sql/script.py",
            "text.txt",
        ]
        criterion = ExcludedExtensionsCriterion(["sql"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)


class TestIncludedDirectoriesCriterion(unittest.TestCase):
    def setUp(self):
        self.samples = [
            "code/scripts/script.py",
            "code/scripts/script.y",
            "code/scripts/sql.sql",
            "code/scripts/sql.txt",
            "code/sql/scripts/script.py",
            "infra/catalog/schema/tab.sql",
            "infra/catalog/sql.py",
            "infra/catalog/sql/script.py",
            "infra/catalog/sql/tab.sql",
            "infra\\catalog\\schema\\script.sql",
            "sql.sql",
            "text.sql",
            "text.txt",
        ]

    def test_apply_empty_filter(self):
        expected = self.samples
        criterion = IncludedDirectoriesCriterion([])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_filter_with_backslash(self):
        expected = [
            "infra/catalog/schema/tab.sql",
            "infra\\catalog\\schema\\script.sql",
        ]
        criterion = IncludedDirectoriesCriterion(["catalog\\schema"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_full_path(self):
        expected = [
            "infra/catalog/sql/script.py",
            "infra/catalog/sql/tab.sql",
        ]
        criterion = IncludedDirectoriesCriterion(["infra/catalog/sql"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_leading_backslash(self):
        expected = [
            "infra/catalog/schema/tab.sql",
            "infra/catalog/sql.py",
            "infra/catalog/sql/script.py",
            "infra/catalog/sql/tab.sql",
            "infra\\catalog\\schema\\script.sql",
        ]
        criterion = IncludedDirectoriesCriterion(["\\infra"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_leading_slash(self):
        expected = [
            "code/scripts/script.py",
            "code/scripts/script.y",
            "code/scripts/sql.sql",
            "code/scripts/sql.txt",
            "code/sql/scripts/script.py",
        ]
        criterion = IncludedDirectoriesCriterion(["/code"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_partial_path(self):
        expected = [
            "code/sql/scripts/script.py",
            "infra/catalog/sql/script.py",
            "infra/catalog/sql/tab.sql",
        ]
        criterion = IncludedDirectoriesCriterion(["sql"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_several_filters(self):
        expected = [
            "code/sql/scripts/script.py",
            "infra/catalog/sql/script.py",
            "infra/catalog/sql/tab.sql",
        ]
        criterion = IncludedDirectoriesCriterion(["catalog/sql", "sql\\"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_trailing_backslash(self):
        expected = [
            "infra/catalog/schema/tab.sql",
            "infra\\catalog\\schema\\script.sql",
        ]
        criterion = IncludedDirectoriesCriterion(["schema/"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_trailing_slash(self):
        expected = [
            "infra/catalog/schema/tab.sql",
            "infra\\catalog\\schema\\script.sql",
        ]
        criterion = IncludedDirectoriesCriterion(["schema\\"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)
