import io
import os
import sys
import webbrowser
from pathlib import Path
import ipfsapi
from ipvc.common import CommonAPI, expand_ref, refpath_to_mfs, make_len, atomic
def __init__(self, *args, **kwargs):...
super().__init__(*args, **kwargs)
@atomic...
_, branch = self.common()
active = self.ipfs.files_read(self.get_mfs_path(self.fs_cwd, repo_info=
    'active_branch_name')).decode('utf-8')
if not self.quiet:
print(active)
return active
