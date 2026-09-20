from zmena.application.handoffs.report_hub.delta_crawler import DeltaCrawlerToReportHubHandoff
from zmena.application.messages.inbound.delta_crawler import DeltaCrawlerInboundMessage
from zmena.application.messages.inbound.semantic_engine import SemanticEngineInboundMessage
from zmena.application.messages.inbound.sql_intake import SQLIntakeInboundMessage
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
    sii_message = SQLIntakeInboundMessage(
        label=dco_message.label,
        name=dco_message.name,
        before=dco_message.before,
        after=dco_message.after,
    )
    pipeline = SQLIntakePipeline(sii_message)
    sio_message = pipeline.run()

    sei_message = SemanticEngineInboundMessage(before=sio_message.before, after=sio_message.after)
    pipeline = SemanticEnginePipeline(sei_message)
    seo_message = pipeline.run()

    handoff = DeltaCrawlerToReportHubHandoff("CMT", dco_message, sio_message, seo_message)
    rhi_message = handoff.prepare()

    report = ReportHub(rhi_message)
    report.show_sql_diff()
    report.show_fragments()
    report.show_hypotheses()
    report.show_components()
    report.show_decisions()
