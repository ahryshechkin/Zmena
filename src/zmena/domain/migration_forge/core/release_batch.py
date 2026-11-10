from datetime import UTC, datetime
from uuid import uuid7


class ReleaseBatch:
    def __init__(self):
        self.run_id = uuid7()
        self.created_at = datetime.now(tz=UTC)

    def __repr__(self):
        return f"ReleaseBatch(run_id={self.run_id})"

    def partition_path(self):
        return (
            f"year={self.created_at:%Y}/"
            f"month={self.created_at:%m}/"
            f"day={self.created_at:%d}/"
            f"run_id={self.run_id}"
        )
