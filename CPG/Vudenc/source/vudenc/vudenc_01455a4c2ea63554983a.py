import os
import sys
from curtin.util import ProcessExecutionError, get_architecture, install_packages, is_uefi_bootable, lsb_release, which
REQUIRED_IMPORTS = [('import yaml', 'python-yaml', 'python3-yaml')]
REQUIRED_EXECUTABLES = [('file', 'file'), ('lvcreate', 'lvm2'), ('mdadm',
    'mdadm'), ('mkfs.vfat', 'dosfstools'), ('mkfs.btrfs', 'btrfs-tools'), (
    'mkfs.ext4', 'e2fsprogs'), ('mkfs.xfs', 'xfsprogs'), ('partprobe',
    'parted'), ('sgdisk', 'gdisk'), ('udevadm', 'udev'), ('make-bcache',
    'bcache-tools'), ('iscsiadm', 'open-iscsi')]
if lsb_release()['codename'] == 'precise':
REQUIRED_IMPORTS.append(('import oauth.oauth', 'python-oauth', None))
REQUIRED_IMPORTS.append(('import oauthlib.oauth1', 'python-oauthlib',
    'python3-oauthlib'))
if not is_uefi_bootable() and 'arm' in get_architecture():
REQUIRED_EXECUTABLES.append(('flash-kernel', 'flash-kernel'))
def __init__(self, message, deps):...
self.message = message
if isinstance(deps, str) or deps is None:
deps = [deps]
self.deps = [d for d in deps if d is not None]
self.fatal = None in deps
def __str__(self):...
if self.fatal:
if not len(self.deps):
return self.message + ' Install packages: %s' % ' '.join(self.deps)
return self.message + ' Unresolvable.'
return self.message + ' Unresolvable.  Partially resolvable with packages: %s' % ' '.join(
    self.deps)
