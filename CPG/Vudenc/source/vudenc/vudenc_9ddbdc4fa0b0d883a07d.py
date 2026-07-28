from __future__ import absolute_import, division, print_function
__metaclass__ = type
from ansible.errors import AnsibleError
""" a group of ansible hosts """
def __init__(self, name=None):...
self.depth = 0
self.name = name
self.hosts = []
self._hosts = None
self.vars = {}
self.child_groups = []
self.parent_groups = []
self._hosts_cache = None
self.priority = 1
def __repr__(self):...
return self.get_name()
