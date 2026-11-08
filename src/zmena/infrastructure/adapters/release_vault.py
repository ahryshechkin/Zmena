from pathlib import Path


class ReleaseVault:
    def __init__(self, message):
        self.message = message

    def save(self):
        path = (Path(self.message.release_path) / self.message.tab_name).with_suffix(".sql")
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open("w", encoding="utf-8") as file:
            file.write(self.message.migration)
