from modules.engine import Engine
from modules.sample import Samples


engine = Engine()
for pair in Samples.get_pairs():
    src = pair["src"].strip().splitlines()
    trg = pair["trg"].strip().splitlines()
    engine.run(src, trg)

