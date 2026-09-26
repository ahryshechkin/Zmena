from zmena.infrastructure.reporting.console.views.statement import StatementView


class StatementProjection:
    def __repr__(self):
        return "StatementProjection(bridges=statement)"

    def apply(self, statement):
        return StatementView(statement)
