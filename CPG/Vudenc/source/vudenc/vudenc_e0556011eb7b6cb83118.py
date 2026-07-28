@Slot()...
"""docstring"""
for language_client in self.clients.values():
if language_client['status'] == self.RUNNING:
folder = self.get_root_path()
inst = language_client['instance']
inst.folder = folder
inst.initialize()
