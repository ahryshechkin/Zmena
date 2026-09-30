from zmena.application.edges.test_suite.records.statement import StatementRecord


class StatementBridge:
    def __repr__(self):
        return "StatementBridge(bridges=statement)"

    def translate(self, statement):
        kind = statement.__class__.__name__
        attrs = statement.__dict__.copy()
        attrs.pop("kind")

        return StatementRecord(kind=kind, attrs=attrs)
