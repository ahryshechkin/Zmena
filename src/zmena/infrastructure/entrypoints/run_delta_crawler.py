from zmena.application.delta_crawler_pipeline import DeltaCrawlerPipeline
from zmena.infrastructure.adapters.commit_catalog import CommitCatalog

catalog = CommitCatalog()
# catalog.build_repo()
# catalog.cleanup()
pipeline = DeltaCrawlerPipeline()
pipeline.run()
