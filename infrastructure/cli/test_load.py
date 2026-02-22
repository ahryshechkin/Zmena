from application.scenario import Scenario

from application import ScenarioCatalog


catalog = ScenarioCatalog()
s = catalog.get("014")

print(s)