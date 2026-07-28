from __future__ import absolute_import, division, print_function
__metaclass__ = type
from ansible.inventory.group import Group
from ansible.utils.vars import combine_vars, get_unique_id
__all__ = ['Host']
""" a single ansible host """
def __getstate__(self):...
return self.serialize()
