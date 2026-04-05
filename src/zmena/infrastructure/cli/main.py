from zmena.application import Pipeline, ScenarioCatalog
from zmena.infrastructure.representation.report_brick import ReportBrick
from zmena.infrastructure.representation.report_component import ReportComponent
from zmena.infrastructure.representation.report_decision import ReportDecision
from zmena.infrastructure.representation.report_hypothesis import ReportHypothesis
from zmena.infrastructure.representation.report_link import ReportLink
from zmena.infrastructure.representation.view import View

sce_ids = ["313"]
catalog = ScenarioCatalog()
for scenario in catalog.get_many(sce_ids):
    pipeline = Pipeline(scenario.before, scenario.after)
    result = pipeline.run()

    view = View(scenario)
    view.show_report()

    ReportBrick(result["bricks"]).render()
    ReportHypothesis(result["hypotheses"]).render()
    ReportComponent(result["components"]).render()
    ReportLink(result["decisions"][0].chosen()).render()
    ReportDecision(result["decisions"]).render()

    # representation.show_bricks(result["bricks"])
    # representation.show_hypotheses(result["hypotheses"])
    # representation.show_components(result["components"])
    # representation.show_decisions(result["decisions"])


# print("")
# catalog.print_scenarios()
