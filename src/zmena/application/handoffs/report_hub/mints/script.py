from zmena.infrastructure.reporting.console.views.script import ScriptView


class ScriptMint:
    def __repr__(self):
        return "ScriptMint(mints=script)"

    def issue(self, script):
        return ScriptView(script.assemble())
