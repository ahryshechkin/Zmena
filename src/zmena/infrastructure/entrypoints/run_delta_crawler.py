from zmena.application.messages.inbound.analysis_report import AnalysisReportInboundMessage
from zmena.application.messages.inbound.delta_crawler import DeltaCrawlerInboundMessage
from zmena.application.messages.inbound.semantic_engine import SemanticEngineInboundMessage
from zmena.application.messages.inbound.sql_intake import SQLIntakeInboundMessage
from zmena.application.pipelines.delta_crawler import DeltaCrawlerPipeline
from zmena.application.pipelines.semantic_engine import SemanticEnginePipeline
from zmena.application.pipelines.sql_intake import SQLIntakePipeline
from zmena.infrastructure.adapters.commit_catalog import CommitCatalog
from zmena.infrastructure.adapters.git_command import GitCommand
from zmena.infrastructure.project_directory import ProjectDirectory
from zmena.infrastructure.representation.analysis_report import AnalysisReport

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

    ari_message = AnalysisReportInboundMessage(
        kind="CMT",
        label=sii_message.label,
        name=sii_message.name,
        before=sio_message.before,
        after=sio_message.after,
        fragments=seo_message.fragments,
        hypotheses=seo_message.hypotheses,
        components=seo_message.components,
        decisions=seo_message.decisions,
    )

    report = AnalysisReport(ari_message)
    report.show_sql_diff()
    report.show_fragments()
    report.show_hypotheses()
    report.show_components()
    report.show_decisions()
