from difflib import SequenceMatcher


class Engine:
    def __init__(self):
        self.sm = SequenceMatcher()


    def run(self, src, trg):
        self.sm.set_seqs(src, trg)
        for tag, slo, shi, tlo, thi in self.sm.get_opcodes():
            print(tag, slo, shi, tlo, thi)
