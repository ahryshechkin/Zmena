from zmena.application.messages.analysis_report import AnalysisReportMessage
from zmena.application.messages.inbound.delta_crawler import DeltaCrawlerInboundMessage
from zmena.application.messages.inbound.semantic_engine import SemanticEngineInboundMessage
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
for sii_message in pipeline.run(command):
    pipeline = SQLIntakePipeline(sii_message)
    sio_message = pipeline.run()

    sei_message = SemanticEngineInboundMessage(before=sio_message.before, after=sio_message.after)

    pipeline = SemanticEnginePipeline(sei_message)
    se_outcome = pipeline.run()

    ar_message = AnalysisReportMessage(
        kind="CMT",
        label=sii_message.label,
        name=sii_message.name,
        before=sio_message.before,
        after=sio_message.after,
        fragments=se_outcome.fragments,
        hypotheses=se_outcome.hypotheses,
        components=se_outcome.components,
        decisions=se_outcome.decisions,
    )

    report = AnalysisReport(ar_message)
    report.show_sql_diff()
    report.show_fragments()
    report.show_hypotheses()
    report.show_components()
    report.show_decisions()
