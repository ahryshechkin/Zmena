from zmena.application.delta_crawler_pipeline import DeltaCrawlerPipeline
from zmena.infrastructure.adapters.commit_catalog import CommitCatalog
from zmena.infrastructure.adapters.git_command import GitCommand
from zmena.infrastructure.project_directory import ProjectDirectory

catalog = CommitCatalog()
catalog.cleanup_demo_repo()
catalog.build_demo_repo()
directory = ProjectDirectory()
command = GitCommand(directory.demo_repo())
pipeline = DeltaCrawlerPipeline("v0.1.001", "v0.1.002")
for before, after in pipeline.run(command):
    print(before)
    print(after)
# catalog.cleanup_demo_repo()
