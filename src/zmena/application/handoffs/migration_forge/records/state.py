from dataclasses import dataclass


@dataclass
class StateRecord:
    name: str
    data_type: str
    nullable: bool

    def __repr__(self):
        return f"StateRecord(name={self.name},data_type={self.data_type},nullable={self.nullable})"
