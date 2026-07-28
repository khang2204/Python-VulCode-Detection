import logging
from pathlib import Path
import psutil
from subprocess import PIPE
import re
def __init__(self, nearest_path=''):...
self.nearest_path = nearest_path
"""
    Parse SSH config files to their basic host details
    """
def __init__(self, file):...
self.file = file
self.hosts = list()
self.parse()
def new_host(self):...
return dict({'host': '', 'hostname': '', 'port': 22, 'username': '',
    'password': '', 'type': 'system'})
