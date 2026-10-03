from zmena.application.handoffs.report_hub.messages.inbound import ReportHubInboundMessage
from zmena.application.handoffs.report_hub.mints.component import ComponentMint
from zmena.application.handoffs.report_hub.mints.decision import DecisionMint
from zmena.application.handoffs.report_hub.mints.evidence import EvidenceMint
from zmena.application.handoffs.report_hub.mints.fragment import FragmentMint
from zmena.application.handoffs.report_hub.mints.hypothesis import HypothesisMint
from zmena.application.handoffs.report_hub.mints.link import LinkMint
from zmena.application.handoffs.report_hub.mints.statement import StatementMint


class ScenarioCatalogToReportHubHandoff:
    def __init__(self, scenario, seo_message, mfo_message=None):
        self.scenario = scenario
        self.seo_message = seo_message
        self.mfo_message = mfo_message

    def __repr__(self):
        return "ScenarioCatalogToReportHubHandoff(messages=sce,seo,mfo)"

    def prepare(self):
        fragment_mint = FragmentMint()
        hypothesis_mint = HypothesisMint(fragment_mint)
        evidence_mint = EvidenceMint()
        component_mint = ComponentMint(fragment_mint, hypothesis_mint)
        decision_mint = DecisionMint(LinkMint(fragment_mint, evidence_mint))
        statement_mint = StatementMint()

        fragments = [fragment_mint.issue(fragment) for fragment in self.seo_message.fragments]
        hypotheses = [
            hypothesis_mint.issue(hypothesis) for hypothesis in self.seo_message.hypotheses
        ]
        components = [component_mint.issue(component) for component in self.seo_message.components]
        decisions = [decision_mint.issue(decision) for decision in self.seo_message.decisions]

        if self.mfo_message is None:
            statements = []
        else:
            statements = [
                statement_mint.issue(statement) for statement in self.mfo_message.statements
            ]

        return ReportHubInboundMessage(
            kind="SCE",
            label=self.scenario.sce_id,
            name=self.scenario.name,
            before=self.scenario.before.splitlines(),
            after=self.scenario.after.splitlines(),
            fragments=fragments,
            hypotheses=hypotheses,
            components=components,
            decisions=decisions,
            statements=statements,
        )
