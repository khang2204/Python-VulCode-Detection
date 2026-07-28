def run_linter(view=None, hook=None):...
"""docstring"""
if not go.ANAGONDA_PRESENT:
return
if get_settings(view, 'anaconda_go_fast_linters_only', False):
fast_linters(view, hook)
all_linters(view, hook)
