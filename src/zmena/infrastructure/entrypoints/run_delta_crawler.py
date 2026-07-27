import os

from zmena.infrastructure.adapters.commit_catalog import CommitCatalog
from zmena.infrastructure.adapters.fs_command import FSCommand
from zmena.infrastructure.adapters.git_command import GitCommand

catalog = CommitCatalog()
fs_command = FSCommand()
fs_command.mkdir("repo")
fs_command.copy("./../../../../catalog/cmt/cmt_001_create_tab01", "repo")
os.chdir("repo")
git_command = GitCommand(".")
git_command.init_repo()
# os.chdir("..")
# fs_command.rmdir("repo")
