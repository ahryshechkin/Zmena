from zmena.application.handoffs.report_hub.delta_crawler import DeltaCrawlerToReportHubHandoff
from zmena.application.handoffs.sematic_engine.sql_intake import SQLIntakeToSemanticEngineHandoff
from zmena.application.handoffs.sql_intake.delta_crawler import DeltaCrawlerToSQLIntakeHandoff
from zmena.application.messages.inbound.delta_crawler import DeltaCrawlerInboundMessage
from zmena.application.pipelines.delta_crawler import DeltaCrawlerPipeline
from zmena.application.pipelines.semantic_engine import SemanticEnginePipeline
from zmena.application.pipelines.sql_intake import SQLIntakePipeline
from zmena.infrastructure.adapters.catalogs.commit import CommitCatalog
from zmena.infrastructure.adapters.commands.git import GitCommand
from zmena.infrastructure.project_directory import ProjectDirectory
from zmena.infrastructure.reporting.console.report_hub import ReportHub

catalog = CommitCatalog()
# catalog.cleanup_demo_repo()
# catalog.build_demo_repo()

directory = ProjectDirectory()
command = GitCommand(directory.demo_repo())

dci_message = DeltaCrawlerInboundMessage(commit_from="v0.1.007", commit_to="v0.1.008")
pipeline = DeltaCrawlerPipeline(dci_message)
for dco_message in pipeline.run(command):
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
