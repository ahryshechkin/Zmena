from zmena.infrastructure import ScenarioCatalog

catalog = ScenarioCatalog()
for scenario in catalog.get_all():
    print(f"SCE-{scenario.sce_id} - {scenario.name.upper()}")
