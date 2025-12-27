from modules.engine import Engine
from modules.sample import Samples


engine = Engine()
for pair in Samples.get_pairs():
    name = pair["name"]
    src = pair["src"].strip().splitlines()
    trg = pair["trg"].strip().splitlines()
    engine.set_width(src, trg)
    engine.run(name, src, trg)

