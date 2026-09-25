from zmena.infrastructure.reporting.console.views.statement import StatementView


class StatementBridge:
    def __repr__(self):
        return "StatementBridge(bridges=statement)"

    def translate(self, statement):
        return StatementView(statement)
