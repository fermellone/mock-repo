import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
ridr_app = git.Repo("../../../penguin/ridr-app/")
ridr_server = git.Repo("../../../penguin/ridr-server/")
ridr_admin = git.Repo("../../../penguin/ridr-admin/")
# Your mock repo
mock_repo = git.Repo("../mock-repo/")
importer = Importer([ridr_app, ridr_server, ridr_admin], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github profiles uses
# my work email
importer.set_author(['fernandomellone2@gmail.com', '38559436+femellone@users.noreply.github.com'])
importer.import_repository()