from datetime import datetime

from zmena.infrastructure.project_directory import ProjectDirectory


class MigrationVault:
    def __init__(self, scripts):
        self.scripts = scripts
        self.directory = ProjectDirectory()

    def generate_path(self):
        now = datetime.now(tz=datetime.timezone.utc)
        print(now.strftime("%H%M%S%f"))
        suffix = f"year={now:%Y}/month={now:%m}/day={now:%d}"

        return self.directory.migrations() / suffix

    def save(self):
        pass
