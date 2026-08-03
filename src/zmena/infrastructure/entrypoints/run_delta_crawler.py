from zmena.application.delta_crawler_pipeline import DeltaCrawlerPipeline
from zmena.infrastructure.adapters.commit_catalog import CommitCatalog
from zmena.infrastructure.adapters.git_command import GitCommand
from zmena.infrastructure.project_directory import ProjectDirectory

catalog = CommitCatalog()
# catalog.build_demo_repo()
directory = ProjectDirectory()
command = GitCommand(directory.demo_repo())
pipeline = DeltaCrawlerPipeline("51a59be", "3aadd15")
pipeline.run(command)
# catalog.cleanup_demo_repo()
