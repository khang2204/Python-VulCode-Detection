def analyze(self):...
self.misc_file_checks()
self.check_helper_consistency()
self.check_source_management()
self.check_manifest()
for script in self.scripts.values():
if script.exists:
script.analyze()
