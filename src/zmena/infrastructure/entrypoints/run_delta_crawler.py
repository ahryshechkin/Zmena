from zmena.infrastructure.adapters.commit_catalog import CommitCatalog
from zmena.infrastructure.adapters.fs_command import FSCommand

catalog = CommitCatalog()
fs_command = FSCommand()
fs_command.mkdir("repo")
fs_command.copy("./../../../../catalog/cmt/cmt_001_create_tab01", "repo")
