from datetime import UTC, datetime
from uuid import uuid7


class PartitionPath:
    def __init__(self):
        self.now = datetime.now(tz=UTC)

    def __repr__(self):
        return f"PartitionPath(now={self.now})"

    def generate(self):
        return f"year={self.now:%Y}/month={self.now:%m}/day={self.now:%d}/{uuid7()}"
