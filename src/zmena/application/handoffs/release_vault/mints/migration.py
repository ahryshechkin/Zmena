class MigrationMint:
    def __repr__(self):
        return "MigrationMint(mints=script)"

    def issue(self, script):
        return script.assemble()
