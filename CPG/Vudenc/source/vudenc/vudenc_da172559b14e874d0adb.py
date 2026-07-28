"""
Manager for all LSP clients connected to the servers defined
in our Preferences.
"""
import logging
import os
from qtpy.QtCore import QObject, Slot
from spyder.config.main import CONF
from spyder.utils.misc import select_port, getcwd_or_home
from spyder.plugins.editor.lsp.client import LSPClient
logger = logging.getLogger(__name__)
"""Language Server Protocol manager."""
STOPPED = 'stopped'
RUNNING = 'running'
def __init__(self, parent):...
QObject.__init__(self)
self.main = parent
self.lsp_plugins = {}
self.clients = {}
self.requests = {}
self.register_queue = {}
self.configurations_for_servers = CONF.options('lsp-server')
for language in self.configurations_for_servers:
self.clients[language] = {'status': self.STOPPED, 'config': CONF.get(
    'lsp-server', language), 'instance': None}
def register_plugin_type(self, type, sig):...
self.register_queue[language] = []
self.lsp_plugins[type] = sig
def register_file(self, language, filename, signal):...
if language in self.clients:
language_client = self.clients[language]['instance']
def get_root_path(self):...
if language_client is None:
"""docstring"""
self.register_queue[language].append((filename, signal))
language_client.register_file(filename, signal)
path = None
if self.main and self.main.projects:
path = self.main.projects.get_active_project_path()
if not path:
path = getcwd_or_home()
return path
