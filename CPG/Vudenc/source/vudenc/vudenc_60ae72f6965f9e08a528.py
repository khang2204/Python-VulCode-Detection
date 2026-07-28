"""
This module provides a mechanism for shutting down virtual storage layers on
top of a block device, making it possible to reuse the block device without
having to reboot the system
"""
import errno
import os
import time
from curtin import block, udev, util
from curtin.block import lvm
from curtin.block import mdadm
from curtin.log import LOG
MDADM_RELEASE_RETRIES = [0.4] * 150
def _define_handlers_registry():...
"""docstring"""
return {'partition': {'shutdown': wipe_superblock, 'ident':
    identify_partition}, 'lvm': {'shutdown': shutdown_lvm, 'ident':
    identify_lvm}, 'crypt': {'shutdown': shutdown_crypt, 'ident':
    identify_crypt}, 'raid': {'shutdown': shutdown_mdadm, 'ident':
    identify_mdadm}, 'bcache': {'shutdown': shutdown_bcache, 'ident':
    identify_bcache}, 'disk': {'ident': lambda x: False, 'shutdown':
    wipe_superblock}}
