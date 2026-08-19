from zmena.application.messages.analysis_report import AnalysisReportMessage
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

pipeline = DeltaCrawlerPipeline("v0.1.004", "v0.1.005")
for si_message in pipeline.run(command):
    pipeline = SQLIntakePipeline(si_message)
    se_message = pipeline.run()

    pipeline = SemanticEnginePipeline(se_message)
    result = pipeline.run()

    ar_message = AnalysisReportMessage(
        kind="CMT",
        label=si_message.label,
        name=si_message.name,
        before=se_message.before,
        after=se_message.after,
        fragments=result.fragments,
        hypotheses=result.hypotheses,
        components=result.components,
        decisions=result.decisions,
    )

    report = AnalysisReport(ar_message)
    report.show_sql_diff()
    report.show_fragments()
    report.show_hypotheses()
    report.show_components()
    report.show_decisions()

# catalog.cleanup_demo_repo()
