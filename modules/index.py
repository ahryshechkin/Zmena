class Index:
    def __init__(self, slo, shi, tlo, thi):
        self.slo = slo
        self.shi = shi
        self.tlo = tlo
        self.thi = thi


    def get(self):
        return f"{self.slo}{self.shi}{self.tlo}{self.thi}"
