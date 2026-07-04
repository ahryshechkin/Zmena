from zmena.infrastructure.adapters.scenario_catalog import ScenarioCatalog

catalog = ScenarioCatalog()
for scenario in catalog.get_all():
    print(f"SCE-{scenario.sce_id} - {scenario.name.upper()}")
