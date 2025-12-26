from modules.engine import Engine
from modules.sample import Samples


RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


def colorize(text, color):
    return f"{color}{text}{RESET}"


engine = Engine()
for pair in Samples.get_pairs():
    src = pair["src"].strip().splitlines()
    trg = pair["trg"].strip().splitlines()
    engine.run(src, trg)

