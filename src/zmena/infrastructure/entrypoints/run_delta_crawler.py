from zmena.application.delta_crawler_pipeline import DeltaCrawlerPipeline
from zmena.infrastructure.adapters.commit_catalog import CommitCatalog
from zmena.infrastructure.adapters.git_command import GitCommand
from zmena.infrastructure.project_directory import ProjectDirectory

catalog = CommitCatalog()
# catalog.cleanup_demo_repo()
# catalog.build_demo_repo()
directory = ProjectDirectory()
command = GitCommand(directory.demo_repo())
pipeline = DeltaCrawlerPipeline("v0.1.003", "v0.1.005")
for message in pipeline.run(command):
    print(message.path)
# catalog.cleanup_demo_repo()
