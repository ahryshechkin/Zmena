from modules.engine import Engine
from modules.sample import Samples
from modules.view import View


engine = Engine()
for sample in Samples.get_pairs():
    src = sample["src"].strip().splitlines()
    trg = sample["trg"].strip().splitlines()
    engine.run(src, trg)
    view = View(sample)
    view.show_report()

print("")
for brick in engine.bricks:
    print(brick)

# print("\n")
# for name in Samples.get_names():
#     print(name)