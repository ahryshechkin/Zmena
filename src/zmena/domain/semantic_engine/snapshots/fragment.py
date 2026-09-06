from dataclasses import dataclass


@dataclass
class FragmentSnapshot:
    name: str
    data_type: str
    nullability: bool
