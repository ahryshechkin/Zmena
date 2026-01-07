from enum import Enum
from textwrap import dedent


class Samples(Enum):
    @classmethod
    def get_pairs(cls):
        pairs = list()

        for sample in Samples:
            if sample not in (Samples.SRC_SHORT, Samples.SRC_LONG):
                pair = {
                    "name": sample.name,
                    "desc": sample.value["desc"],
                    "src": Samples.SRC_LONG.value if sample.name == "SML_12" else Samples.SRC_SHORT.value,
                    "trg": sample.value["text"],
                }
                pairs.append(pair)

        return pairs


    @classmethod
    def get_names(cls):
        names = list()

        for sample in Samples:
            if sample not in (Samples.SRC_SHORT, Samples.SRC_LONG):
                names.append(sample.value["desc"])

        return names


    SRC_SHORT = dedent("""
        col_01 int not null,
        col_02 varchar(50) not null,
        col_03 varchar(200),
        col_04 varchar(50) not null,
        col_05 varchar(50),
        col_06 int,
        col_07 varchar(1) not null,
        col_08 date not null,
        col_09 datetime2 not null,
        col_10 datetime2 not null
    """).strip("\n")

    SRC_LONG = dedent("""
        col_01 int not null,
        col_02 varchar(50) not null,
        col_03 varchar(200),
        col_04 varchar(50) not null,
        col_05 varchar(50),
        col_06 int,
        col_07 varchar(1) not null,
        col_08 date not null,
        col_09 datetime2 not null,
        col_10 datetime2 not null,
        col_11 int not null,
        col_12 varchar(50) not null,
        col_13 varchar(200),
        col_14 varchar(50) not null,
        col_15 varchar(50),
        col_16 int,
        col_17 varchar(1) not null,
        col_18 date not null,
        col_19 datetime2 not null,
        col_20 datetime2 not null
    """).strip("\n")

    SML_011 = {
        "desc": "ADD_COLUMN_NOT_NULL",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(200),
            col_04 varchar(50) not null,
            col_05 varchar(50),
            col_06 int,
            col_07 varchar(1) not null,
            col_08 date not null,
            col_88 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_012 = {
        "desc": "ADD_COLUMN_NULL",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(200),
            col_33 varchar(200),
            col_04 varchar(50) not null,
            col_05 varchar(50),
            col_06 int,
            col_07 varchar(1) not null,
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_013 = {
        "desc": "ALTER_CONSTRAINT_NOT_NULL",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(200),
            col_04 varchar(50) not null,
            col_05 varchar(50),
            col_06 int not null,
            col_07 varchar(1) not null,
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_014 = {
        "desc": "ALTER_CONSTRAINT_NULL",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(200),
            col_04 varchar(50) not null,
            col_05 varchar(50),
            col_06 int,
            col_07 varchar(1),
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_015 = {
        "desc": "CHANGE_DATA_TYPE",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(200),
            col_04 varchar(50) not null,
            col_05 varchar(50),
            col_06 int,
            col_07 varchar(1) not null,
            col_08 datetime2 not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_016 = {
        "desc": "DROP_COLUMN",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(200),
            col_04 varchar(50) not null,
            col_05 varchar(50),
            col_07 varchar(1) not null,
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_017 = {
        "desc": "MOVE_COLUMN",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(200),
            col_07 varchar(1) not null,
            col_04 varchar(50) not null,
            col_05 varchar(50),
            col_06 int,
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_018 = {
        "desc": "RENAME_COLUMN",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(200),
            col_04 varchar(50) not null,
            col_05 varchar(50),
            col_06 int,
            col_77 varchar(1) not null,
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_051 = {
        "desc": "ALTER_COLUMN_AND_ADD_ANOTHER_AFTER",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(200) not null,
            col_33 varchar(200),
            col_04 varchar(50) not null,
            col_05 varchar(50),
            col_06 int,
            col_07 varchar(1) not null,
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_052 = {
        "desc": "ALTER_COLUMN_AND_ADD_ANOTHER_BEFORE",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_22 varchar(50) not null,
            col_03 varchar(200) not null,
            col_04 varchar(50) not null,
            col_05 varchar(50),
            col_06 int,
            col_07 varchar(1) not null,
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_053 = {
        "desc": "ALTER_COLUMN_AND_RENAME_TWO_ADJACENT_ONES",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(20),
            col_44 varchar(50) not null,
            col_55 varchar(50),
            col_06 int,
            col_07 varchar(1) not null,
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_151 = {
        "desc": "APPLY_SCRIPTS_IN_PROPER_ORDER",
        "text": dedent("""
            col_01 int not null,
            col_05 varchar(50) not null,
            col_03 varchar(200),
            col_04 varchar(50) not null,
            col_06 int,
            col_08 int,
            col_07 varchar(1) not null,
            col_88 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_301 = {
        "desc": "MOVE_COLUMN_AFTER_SINGLE_CONSTRAINT_AND_TYPE_ALTER",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(200),
            col_04 date,
            col_07 varchar(1) not null,
            col_05 varchar(50),
            col_06 int,
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_302 = {
        "desc": "MOVE_COLUMN_AFTER_TWO_CONSTRAINT_AND_TYPE_ALTER",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(200),
            col_04 date,
            col_05 date not null,
            col_07 varchar(1) not null,
            col_06 int,
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_321 = {
        "desc": "MOVE_COLUMN_BEFORE_SINGLE_CONSTRAINT_ALTER",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(200),
            col_07 varchar(1) not null,
            col_04 varchar(50),
            col_05 varchar(50),
            col_06 int,
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_322 = {
        "desc": "MOVE_COLUMN_BEFORE_SINGLE_TYPE_ALTER",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(200),
            col_07 varchar(1) not null,
            col_04 date not null,
            col_05 varchar(50),
            col_06 int,
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_333 = {
        "desc": "MOVE_COLUMN_BEFORE_SINGLE_CONSTRAINT_AND_TYPE_ALTER",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(200),
            col_07 varchar(1) not null,
            col_04 date,
            col_05 varchar(50),
            col_06 int,
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_351 = {
        "desc": "MOVE_COLUMN_BEFORE_TWO_CONSTRAINT_ALTER",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(200),
            col_07 varchar(1) not null,
            col_04 varchar(50),
            col_05 varchar(50) not null,
            col_06 int,
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_352 = {
        "desc": "MOVE_COLUMN_BEFORE_TWO_TYPE_ALTER",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(200),
            col_07 varchar(1) not null,
            col_04 date not null,
            col_05 date,
            col_06 int,
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_353 = {
        "desc": "MOVE_COLUMN_BEFORE_TWO_CONSTRAINT_AND_TYPE_ALTER",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(200),
            col_07 varchar(1) not null,
            col_04 date,
            col_05 date not null,
            col_06 int,
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_401 = {
        "desc": "MOVE_TWO_COLUMNS_AFTER_ALTERED_ONE",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(200),
            col_04 varchar(50),
            col_07 varchar(1) not null,
            col_08 date not null,
            col_05 varchar(50),
            col_06 int,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_402 = {
        "desc": "MOVE_TWO_COLUMNS_BEFORE_ALTERED_ONE",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(200),
            col_07 varchar(1) not null,
            col_08 date not null,
            col_04 varchar(50),
            col_05 varchar(50),
            col_06 int,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_403 = {
        "desc": "MOVE_TWO_COLUMNS_BEFORE_ALTERED_ONE_TWICE",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_03 varchar(200),
            col_07 varchar(1) not null,
            col_08 date not null,
            col_04 varchar(51) not null,
            col_05 varchar(50),
            col_06 int,
            col_09 datetime2 not null,
            col_10 datetime2 not null,
            col_11 int not null,
            col_12 varchar(50) not null,
            col_13 varchar(200),
            col_17 varchar(1) not null,
            col_18 date not null,
            col_14 varchar(51) not null,
            col_15 varchar(50),
            col_16 int,
            col_19 datetime2 not null,
            col_20 datetime2 not null
        """).strip("\n"),
    }

    SML_501 = {
        "desc": "PERFORM_SEVERAL_SIMPLE_CHANGES",
        "text": dedent("""
            col_01 int not null,
            col_11 int,
            col_22 varchar(50) not null,
            col_02 varchar(50) not null,
            col_03 varchar(200),
            col_04 varchar(50) not null,
            col_05 varchar(50),
            col_06 int,
            col_07 varchar(10) not null,
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_601 = {
        "desc": "RENAME_COLUMN_AND_MOVE_ANOTHER_AFTER_FROM_BOTTOM",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_33 varchar(200),
            col_07 varchar(1) not null,
            col_04 varchar(50) not null,
            col_05 varchar(50),
            col_06 int,
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_602 = {
        "desc": "RENAME_COLUMN_AND_MOVE_ANOTHER_AFTER_FROM_TOP",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_04 varchar(50) not null,
            col_05 varchar(50),
            col_06 int,
            col_77 varchar(1) not null,
            col_03 varchar(200),
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_603 = {
        "desc": "RENAME_COLUMN_AND_MOVE_ANOTHER_BEFORE_FROM_BOTTOM",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_07 varchar(1) not null,
            col_33 varchar(200),
            col_04 varchar(50) not null,
            col_05 varchar(50),
            col_06 int,
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }


    SML_604 = {
        "desc": "RENAME_COLUMN_AND_MOVE_ANOTHER_BEFORE_FROM_TOP",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_04 varchar(50) not null,
            col_05 varchar(50),
            col_06 int,
            col_03 varchar(200),
            col_77 varchar(1) not null,
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_651 = {
        "desc": "RENAME_COLUMN_TO_DELETED_NAME_FROM_BOTTOM",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_07 varchar(200),
            col_04 varchar(50) not null,
            col_05 varchar(50),
            col_06 int,
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_652 = {
        "desc": "RENAME_COLUMN_TO_DELETED_NAME_FROM_TOP",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_04 varchar(50) not null,
            col_05 varchar(50),
            col_06 int,
            col_03 varchar(1) not null,
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_701 = {
        "desc": "SWAP_COLUMNS",
        "text": dedent("""
            col_01 int not null,
            col_02 varchar(50) not null,
            col_07 varchar(1) not null,
            col_04 varchar(50) not null,
            col_05 varchar(50),
            col_06 int,
            col_03 varchar(200),
            col_08 date not null,
            col_09 datetime2 not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_702 = {
        "desc": "SWAP_COLUMNS_NESTED",
        "text": dedent("""
            col_01 int not null,
            col_09 datetime2 not null,
            col_03 varchar(200),
            col_06 int,
            col_05 varchar(50),
            col_04 varchar(50) not null,
            col_07 varchar(1) not null,
            col_08 date not null,
            col_02 varchar(50) not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }

    SML_703 = {
        "desc": "SWAP_COLUMNS_WITH_OVERLAP",
        "text": dedent("""
            col_01 int not null,
            col_06 int,
            col_03 varchar(200),
            col_09 datetime2 not null,
            col_05 varchar(50),
            col_02 varchar(50) not null,
            col_07 varchar(1) not null,
            col_08 date not null,
            col_04 varchar(50) not null,
            col_10 datetime2 not null
        """).strip("\n"),
    }