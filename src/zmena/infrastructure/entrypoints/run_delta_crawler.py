from zmena.application.messages.analysis_report import AnalysisReportMessage
from zmena.application.messages.delta_crawler import DeltaCrawlerMessage
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

dc_message = DeltaCrawlerMessage(commit_from="v0.1.007", commit_to="v0.1.008")

pipeline = DeltaCrawlerPipeline(dc_message)
for si_message in pipeline.run(command):
    pipeline = SQLIntakePipeline(si_message)
    se_message = pipeline.run()

    pipeline = SemanticEnginePipeline(se_message)
    se_outcome = pipeline.run()

    ar_message = AnalysisReportMessage(
        kind="CMT",
        label=si_message.label,
        name=si_message.name,
        before=se_message.before,
        after=se_message.after,
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
