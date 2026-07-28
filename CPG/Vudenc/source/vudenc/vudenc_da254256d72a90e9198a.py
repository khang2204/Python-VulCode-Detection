"""
Module for gathering disk information
"""
import logging
import salt.utils
log = logging.getLogger(__name__)
def __virtual__():...
"""docstring"""
if salt.utils.is_windows():
return False
return 'disk'
