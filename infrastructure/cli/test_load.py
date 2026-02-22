from application.scenario import Scenario

from application import ScenarioCatalog


scenario_catalog = ScenarioCatalog()
s = scenario_catalog.get(["151", "014"])

print(s)