from dataclasses import fields

from zmena.application.edges.report_hub.records.statement import StatementRecord


class StatementBridge:
    def __repr__(self):
        return "StatementBridge(bridges=statement)"

    def translate(self, statement):
        return StatementRecord(
            name=statement.__class__.__name__,
            attributes={field.name: getattr(statement, field.name) for field in fields(statement)},
        )
