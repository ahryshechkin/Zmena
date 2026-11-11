from zmena.application.handoffs.delta_crawler.from_commit_catalog import (
    CommitCatalogToDeltaCrawlerHandoff,
)
from zmena.application.handoffs.report_hub.from_delta_crawler import (
    DeltaCrawlerToReportHubHandoff,
)
from zmena.application.handoffs.semantic_engine.from_sql_intake import (
    SQLIntakeToSemanticEngineHandoff,
)
from zmena.application.handoffs.sql_intake.from_delta_crawler import (
    DeltaCrawlerToSQLIntakeHandoff,
)
from zmena.application.pipelines.delta_crawler import DeltaCrawlerPipeline
from zmena.application.pipelines.semantic_engine import SemanticEnginePipeline
from zmena.application.pipelines.sql_intake import SQLIntakePipeline
from zmena.infrastructure.adapters.catalogs.commit import CommitCatalog
from zmena.infrastructure.reporting.console.report_hub import ReportHub

catalog = CommitCatalog()
# catalog.cleanup_demo_repo()
# catalog.build_demo_repo()

handoff = CommitCatalogToDeltaCrawlerHandoff("v0.1.008", "v0.1.009")
dci_message = handoff.prepare()

pipeline = DeltaCrawlerPipeline(dci_message)
for dco_message in pipeline.run():
    handoff = DeltaCrawlerToSQLIntakeHandoff(dco_message)
    sii_message = handoff.prepare()

    pipeline = SQLIntakePipeline(sii_message)
    sio_message = pipeline.run()

    handoff = SQLIntakeToSemanticEngineHandoff(sio_message)
    sei_message = handoff.prepare()

    pipeline = SemanticEnginePipeline(sei_message)
    seo_message = pipeline.run()

    handoff = DeltaCrawlerToReportHubHandoff(dco_message, sio_message, seo_message)
    rhi_message = handoff.prepare()

    report = ReportHub(rhi_message)
    report.show_sql_diff()
    report.show_fragments()
    report.show_hypotheses()
    report.show_components()
    report.show_decisions()
    report.show_statements()
    report.show_scripts()
