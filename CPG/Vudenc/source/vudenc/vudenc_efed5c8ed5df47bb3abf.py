def check_build_for_current_platform_only(self, targets):...
"""docstring"""
if not self._any_targets_have_native_sources(targets):
return False
platforms_with_sources = pex_build_util.targets_by_platform(targets, self.
    _python_setup)
platform_names = list(platforms_with_sources.keys())
if not platform_names or platform_names == ['current']:
return True
bad_targets = set()
for platform, targets in platforms_with_sources.items():
if platform == 'current':
bad_targets.update(targets)
