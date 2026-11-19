import unittest

from zmena.domain.delta_crawler.core.diff_entry import DiffEntry
from zmena.domain.delta_crawler.criteria.criterion import Criterion
from zmena.domain.delta_crawler.criteria.excluded_directories import ExcludedDirectoriesCriterion
from zmena.domain.delta_crawler.criteria.excluded_extensions import ExcludedExtensionsCriterion
from zmena.domain.delta_crawler.criteria.included_directories import IncludedDirectoriesCriterion
from zmena.domain.delta_crawler.criteria.included_extensions import IncludedExtensionsCriterion
from zmena.domain.delta_crawler.kinds.criterion import CriterionKind


class TestCriterion(unittest.TestCase):
    def setUp(self):
        self.criterion = Criterion(CriterionKind.UNDEFINED)

    def test_init_execution(self):
        self.assertEqual(CriterionKind.UNDEFINED, self.criterion.kind)

    def test_repr_execution(self):
        self.assertEqual("Criterion(kind=undefined)", repr(self.criterion))


class TestExcludedDirectoriesCriterion(unittest.TestCase):
    def setUp(self):
        self.criterion = ExcludedDirectoriesCriterion([])
        self.entries = [
            DiffEntry(entry)
            for entry in [
                "M\tcode/scripts/script.py",
                "M\tcode/scripts/script.y",
                "M\tcode/scripts/sql.sql",
                "M\tcode/scripts/sql.txt",
                "M\tcode/sql/scripts/script.py",
                "M\tinfra/catalog/schema/tab.sql",
                "M\tinfra/catalog/sql.py",
                "M\tinfra/catalog/sql/script.py",
                "M\tinfra/catalog/sql/tab.sql",
                "M\tinfra\\catalog\\schema\\script.sql",
                "M\tsql.sql",
                "M\ttext.sql",
                "M\ttext.txt",
            ]
        ]

    def test_apply_empty_filter(self):
        expected = self.entries
        criterion = ExcludedDirectoriesCriterion([])
        actual = criterion.apply(self.entries)

        self.assertCountEqual(expected, actual)

    def test_apply_filter_with_backslash(self):
        expected = [
            DiffEntry(entry)
            for entry in [
                "M\tcode/scripts/script.py",
                "M\tcode/scripts/script.y",
                "M\tcode/scripts/sql.sql",
                "M\tcode/scripts/sql.txt",
                "M\tcode/sql/scripts/script.py",
                "M\tinfra/catalog/sql.py",
                "M\tinfra/catalog/sql/script.py",
                "M\tinfra/catalog/sql/tab.sql",
                "M\tsql.sql",
                "M\ttext.sql",
                "M\ttext.txt",
            ]
        ]
        criterion = ExcludedDirectoriesCriterion(["catalog\\schema"])
        actual = criterion.apply(self.entries)

        self.assertCountEqual(
            [entry.path() for entry in expected],
            [entry.path() for entry in actual],
        )

    def test_apply_full_path(self):
        expected = [
            DiffEntry(entry)
            for entry in [
                "M\tcode/scripts/script.py",
                "M\tcode/scripts/script.y",
                "M\tcode/scripts/sql.sql",
                "M\tcode/scripts/sql.txt",
                "M\tcode/sql/scripts/script.py",
                "M\tinfra/catalog/schema/tab.sql",
                "M\tinfra/catalog/sql.py",
                "M\tinfra\\catalog\\schema\\script.sql",
                "M\tsql.sql",
                "M\ttext.sql",
                "M\ttext.txt",
            ]
        ]
        criterion = ExcludedDirectoriesCriterion(["infra/catalog/sql"])
        actual = criterion.apply(self.entries)

        self.assertCountEqual(
            [entry.path() for entry in expected],
            [entry.path() for entry in actual],
        )

    def test_apply_leading_backslash(self):
        expected = [
            DiffEntry(entry)
            for entry in [
                "M\tcode/scripts/script.py",
                "M\tcode/scripts/script.y",
                "M\tcode/scripts/sql.sql",
                "M\tcode/scripts/sql.txt",
                "M\tcode/sql/scripts/script.py",
                "M\tsql.sql",
                "M\ttext.sql",
                "M\ttext.txt",
            ]
        ]
        criterion = ExcludedDirectoriesCriterion(["\\infra"])
        actual = criterion.apply(self.entries)

        self.assertCountEqual(
            [entry.path() for entry in expected],
            [entry.path() for entry in actual],
        )

    def test_apply_leading_slash(self):
        expected = [
            DiffEntry(entry)
            for entry in [
                "M\tinfra/catalog/schema/tab.sql",
                "M\tinfra/catalog/sql.py",
                "M\tinfra/catalog/sql/script.py",
                "M\tinfra/catalog/sql/tab.sql",
                "M\tinfra\\catalog\\schema\\script.sql",
                "M\tsql.sql",
                "M\ttext.sql",
                "M\ttext.txt",
            ]
        ]
        criterion = ExcludedDirectoriesCriterion(["/code"])
        actual = criterion.apply(self.entries)

        self.assertCountEqual(
            [entry.path() for entry in expected],
            [entry.path() for entry in actual],
        )

    def test_apply_partial_path(self):
        expected = [
            DiffEntry(entry)
            for entry in [
                "M\tcode/scripts/script.py",
                "M\tcode/scripts/script.y",
                "M\tcode/scripts/sql.sql",
                "M\tcode/scripts/sql.txt",
                "M\tinfra/catalog/schema/tab.sql",
                "M\tinfra/catalog/sql.py",
                "M\tinfra\\catalog\\schema\\script.sql",
                "M\tsql.sql",
                "M\ttext.sql",
                "M\ttext.txt",
            ]
        ]
        criterion = ExcludedDirectoriesCriterion(["sql"])
        actual = criterion.apply(self.entries)

        self.assertCountEqual(
            [entry.path() for entry in expected],
            [entry.path() for entry in actual],
        )

    def test_apply_several_filters(self):
        expected = [
            DiffEntry(entry)
            for entry in [
                "M\tcode/scripts/script.py",
                "M\tcode/scripts/script.y",
                "M\tcode/scripts/sql.sql",
                "M\tcode/scripts/sql.txt",
                "M\tinfra/catalog/schema/tab.sql",
                "M\tinfra/catalog/sql.py",
                "M\tinfra\\catalog\\schema\\script.sql",
                "M\tsql.sql",
                "M\ttext.sql",
                "M\ttext.txt",
            ]
        ]
        criterion = ExcludedDirectoriesCriterion(["catalog/sql", "sql\\"])
        actual = criterion.apply(self.entries)

        self.assertCountEqual(
            [entry.path() for entry in expected],
            [entry.path() for entry in actual],
        )

    def test_apply_trailing_backslash(self):
        expected = [
            DiffEntry(entry)
            for entry in [
                "M\tcode/scripts/script.py",
                "M\tcode/scripts/script.y",
                "M\tcode/scripts/sql.sql",
                "M\tcode/scripts/sql.txt",
                "M\tcode/sql/scripts/script.py",
                "M\tinfra/catalog/sql.py",
                "M\tinfra/catalog/sql/script.py",
                "M\tinfra/catalog/sql/tab.sql",
                "M\tsql.sql",
                "M\ttext.sql",
                "M\ttext.txt",
            ]
        ]
        criterion = ExcludedDirectoriesCriterion(["schema/"])
        actual = criterion.apply(self.entries)

        self.assertCountEqual(
            [entry.path() for entry in expected],
            [entry.path() for entry in actual],
        )

    def test_apply_trailing_slash(self):
        expected = [
            DiffEntry(entry)
            for entry in [
                "M\tcode/scripts/script.py",
                "M\tcode/scripts/script.y",
                "M\tcode/scripts/sql.sql",
                "M\tcode/scripts/sql.txt",
                "M\tcode/sql/scripts/script.py",
                "M\tinfra/catalog/sql.py",
                "M\tinfra/catalog/sql/script.py",
                "M\tinfra/catalog/sql/tab.sql",
                "M\tsql.sql",
                "M\ttext.sql",
                "M\ttext.txt",
            ]
        ]
        criterion = ExcludedDirectoriesCriterion(["schema\\"])
        actual = criterion.apply(self.entries)

        self.assertCountEqual(
            [entry.path() for entry in expected],
            [entry.path() for entry in actual],
        )

    def test_init_execution(self):
        self.assertEqual(CriterionKind.EXCLUDED_DIRECTORIES, self.criterion.kind)

    def test_repr_execution(self):
        self.assertEqual("Criterion(kind=excluded directories)", repr(self.criterion))


class TestExcludedExtensionsCriterion(unittest.TestCase):
    def setUp(self):
        self.criterion = ExcludedExtensionsCriterion([])
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

    def test_init_execution(self):
        self.assertEqual(CriterionKind.EXCLUDED_EXTENSIONS, self.criterion.kind)

    def test_repr_execution(self):
        self.assertEqual("Criterion(kind=excluded extensions)", repr(self.criterion))


class TestIncludedDirectoriesCriterion(unittest.TestCase):
    def setUp(self):
        self.criterion = IncludedDirectoriesCriterion([])
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

    def test_init_execution(self):
        self.assertEqual(CriterionKind.INCLUDED_DIRECTORIES, self.criterion.kind)

    def test_repr_execution(self):
        self.assertEqual("Criterion(kind=included directories)", repr(self.criterion))


class TestIncludedExtensionsCriterion(unittest.TestCase):
    def setUp(self):
        self.criterion = IncludedExtensionsCriterion([])
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
        criterion = IncludedExtensionsCriterion([])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_partial_extension(self):
        expected = [
            "code/scripts/script.y",
        ]
        criterion = IncludedExtensionsCriterion(["y"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_several_extensions(self):
        expected = [
            "code/scripts/sql.sql",
            "infra/catalog/schema/tab.sql",
            "infra/catalog/sql/tab.sql",
            "infra\\catalog\\schema\\script.sql",
            "sql.sql",
            "text.sql",
        ]
        criterion = IncludedExtensionsCriterion([".sql"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_single_extension(self):
        expected = [
            "code/scripts/script.py",
            "code/scripts/sql.txt",
            "code/sql/scripts/script.py",
            "infra/catalog/sql.py",
            "infra/catalog/sql/script.py",
            "text.txt",
        ]
        criterion = IncludedExtensionsCriterion([".py", ".txt"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_apply_suffix_only(self):
        expected = [
            "code/scripts/sql.sql",
            "infra/catalog/schema/tab.sql",
            "infra/catalog/sql/tab.sql",
            "infra\\catalog\\schema\\script.sql",
            "sql.sql",
            "text.sql",
        ]
        criterion = IncludedExtensionsCriterion(["sql"])
        actual = criterion.apply(self.samples)

        self.assertCountEqual(expected, actual)

    def test_init_execution(self):
        self.assertEqual(CriterionKind.INCLUDED_EXTENSIONS, self.criterion.kind)

    def test_repr_execution(self):
        self.assertEqual("Criterion(kind=included extensions)", repr(self.criterion))
