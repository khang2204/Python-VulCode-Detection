def analyze(self):...
print_header(self.name.upper() + ' SCRIPT')
self.check_verifications_done_before_modifying_system()
self.check_set_usage()
self.check_helper_usage_dependencies()
self.check_deprecated_practices()
