from zmena.application.messages.inbound.analysis_report import AnalysisReportInboundMessage
from zmena.application.messages.inbound.semantic_engine import SemanticEngineInboundMessage
from zmena.application.pipelines.semantic_engine import SemanticEnginePipeline
from zmena.domain.semantic_engine.projections.decision import DecisionProjection
from zmena.domain.semantic_engine.projections.fragment import FragmentProjection
from zmena.domain.semantic_engine.projections.link import LinkProjection
from zmena.infrastructure.adapters.catalogs.scenario import ScenarioCatalog
from zmena.infrastructure.representation.analysis_report import AnalysisReport

sce_ids = ["011"]
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    sei_message = SemanticEngineInboundMessage(
        before=scenario.before.splitlines(), after=scenario.after.splitlines()
    )
    pipeline = SemanticEnginePipeline(sei_message)
    seo_message = pipeline.run()

    ari_message = AnalysisReportInboundMessage(
        kind="SCE",
        label=scenario.sce_id,
        name=scenario.name,
        before=scenario.before.splitlines(),
        after=scenario.after.splitlines(),
        fragments=seo_message.fragments,
        hypotheses=seo_message.hypotheses,
        components=seo_message.components,
        decisions=seo_message.decisions,
    )

    decision = seo_message.decisions[0]
    projection = DecisionProjection(LinkProjection(FragmentProjection()))
    snapshot = projection.from_domain(decision)

    report = AnalysisReport(ari_message)
    report.show_sql_diff()
    report.show_fragments()
    report.show_hypotheses()
    report.show_components()
    report.show_decisions()
