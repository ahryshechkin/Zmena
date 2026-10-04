from dataclasses import fields

from zmena.application.handoffs.test_suite.records.statement import StatementRecord


class StatementMint:
    def __repr__(self):
        return "StatementMint(mints=statement)"

    def issue(self, statement):
        kind = statement.__class__.__name__
        attrs = {field.name: getattr(statement, field.name) for field in fields(statement)}

        return StatementRecord(kind, attrs)
