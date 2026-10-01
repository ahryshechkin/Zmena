from dataclasses import fields

from zmena.application.edges.test_suite.records.statement import StatementRecord


class StatementBridge:
    def __repr__(self):
        return "StatementBridge(bridges=statement)"

    def translate(self, statement):
        kind = statement.__class__.__name__
        attrs = {field.name: getattr(statement, field.name) for field in fields(statement)}

        return StatementRecord(kind=kind, attrs=attrs)
