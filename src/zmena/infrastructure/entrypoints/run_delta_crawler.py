from zmena.infrastructure.adapters.commit_catalog import CommitCatalog
from zmena.infrastructure.adapters.fs_command import FSCommand
from zmena.infrastructure.adapters.git_command import GitCommand
from zmena.infrastructure.project_directory import ProjectDirectory

catalog = CommitCatalog()
directory = ProjectDirectory()
fs_command = FSCommand(directory.test_repo())
git_command = GitCommand(directory.test_repo())
fs_command.mkdir()
git_command.init()
fs_command.copy(f"{directory.cmt()}/cmt_001_create_tab01")
git_command.add()
git_command.commit()
fs_command.copy(f"{directory.cmt()}/cmt_002_add_column_tab01")
git_command.add()
git_command.commit()
fs_command.copy(f"{directory.cmt()}/cmt_003_create_tab02")
git_command.add()
git_command.commit()
fs_command.copy(f"{directory.cmt()}/cmt_004_rename_column_tab02")
git_command.add()
git_command.commit()
fs_command.copy(f"{directory.cmt()}/cmt_005_update_tab01_and_tab02")
git_command.add()
git_command.commit()
fs_command.rmdir()
