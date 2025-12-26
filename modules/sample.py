from enum import Enum
from textwrap import dedent


class Samples(Enum):
    @classmethod
    def get_pairs(cls):
        pairs = list()

        for sample in Samples:
            if sample != Samples.SRC:
                pair = {
                    "src": Samples.SRC.value,
                    "trg": sample.value,
                }
                pairs.append(pair)

        return pairs


    SRC = dedent("""
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

    TRG_01 = dedent("""
        col_01 int not null,
        col_02 varchar(50) not null,
        col_03 varchar(200),
        col_33 varchar(200),
        col_04 varchar(50) not null,
        col_05 varchar(51),
        col_06 int,
        col_66 int,
        col_07 varchar(1) not null,
        col_08 date not null,
        col_10 datetime2 not null
    """).strip("\n")

    TRG_02 = dedent("""
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
