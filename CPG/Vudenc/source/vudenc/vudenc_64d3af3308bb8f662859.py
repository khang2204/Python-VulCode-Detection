def all_linters(view=None, hook=None):...
"""docstring"""
if view is None:
view = active_view()
if not get_settings(view, 'anaconda_go_linting', True):
return
if view.file_name() in anaconda_sublime.ANACONDA['DISABLED']:
anaconda_sublime.erase_lint_marks(view)
settings = _get_settings(view)
return
data = {'vid': view.id(), 'code': view.substr(st3_sublime.Region(0, view.
    size())), 'settings': settings, 'filepath': view.file_name(), 'method':
    'all_lint', 'handler': 'anaGonda', 'go_env': {'GOROOT': go.GOROOT,
    'GOPATH': go.GOPATH, 'CGO_ENABLED': go.CGO_ENABLED}}
callback = partial(anaconda_sublime.parse_results, **dict(code='go'))
if hook is None:
Worker().execute(Callback(on_success=callback), **data)
Worker().execute(Callback(partial(hook, callback)), **data)
