from datetime import UTC, datetime
from uuid import uuid7


class PartitionPath:
    def __repr__(self):
        return "PartitionPath"

    def generate(self):
        now = datetime.now(tz=UTC)
        return f"year={now:%Y}/month={now:%m}/day={now:%d}/{uuid7()}"
