from enum import Enum
from textwrap import dedent


class Samples(Enum):
    @classmethod
    def get_pairs(cls):
        pairs = list()

        for sample in Samples:
            if sample != Samples.BASE:
                pair = {
                    "name": sample.value["name"],
                    "src": Samples.BASE.value,
                    "trg": sample.value["text"],
                }
                pairs.append(pair)

        return pairs


    BASE = dedent("""
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

    SML_01 = {
        "name": "ADD_COLUMN_NOT_NULL",
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

    SML_02 = {
        "name": "ADD_COLUMN_NULL",
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

    SML_03 = {
        "name": "ALTER_CONSTRAINT_NOT_NULL",
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

    SML_04 = {
        "name": "ALTER_CONSTRAINT_NULL",
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

    SML_05 = {
        "name": "CHANGE_DATA_TYPE",
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

    SML_06 = {
        "name": "DROP_COLUMN",
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

    SML_07 = {
        "name": "MOVE_COLUMN",
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

    SML_08 = {
        "name": "RENAME_COLUMN",
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

    SML_09 = {
        "name": "MAKE_SEVERAL_CHANGES",
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

    SML_10 = {
        "name": "MOVE_DOWN_TO_RENAMED_PLACE",
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

    SML_11 = {
        "name": "MOVE_UP_TO_RENAMED_PLACE",
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

    SML_12 = {
        "name": "MOVE_WITH_DOUBLE_CONSTRAINT_ALTER",
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

    SML_13 = {
        "name": "MOVE_WITH_DOUBLE_CONSTRAINT_ALTER",
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

    SML_14 = {
        "name": "MOVE_WITH_DOUBLE_TYPE_CONSTRAINT_ALTER",
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

    SML_15 = {
        "name": "MOVE_WITH_SINGLE_CONSTRAINT_ALTER",
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

    SML_16 = {
        "name": "MOVE_WITH_SINGLE_TYPE_ALTER",
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

    SML_17 = {
        "name": "MOVE_WITH_SINGLE_TYPE_CONSTRAINT_ALTER",
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

    SML_18 = {
        "name": "ORGANIZE_SCRIPTS_IN_PROPER_ORDER",
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

    SML_19 = {
        "name": "PERFORM_ALTER_AND_RENAME_NEXT_TO",
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

    SML_20 = {
        "name": "RENAME_DOWN_AS_DELETED_COLUMN",
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

    SML_21 = {
        "name": "RENAME_UP_AS_DELETED_COLUMN",
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

    SML_22 = {
        "name": "SWAP_COLUMNS",
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