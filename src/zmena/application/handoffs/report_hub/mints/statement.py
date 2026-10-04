from dataclasses import fields

from zmena.infrastructure.reporting.console.views.statement import StatementView


class StatementMint:
    def __repr__(self):
        return "StatementMint(mints=statement)"

    def issue(self, statement):
        kind = statement.__class__.__name__
        attrs = {field.name: getattr(statement, field.name) for field in fields(statement)}

        return StatementView(kind, attrs)
