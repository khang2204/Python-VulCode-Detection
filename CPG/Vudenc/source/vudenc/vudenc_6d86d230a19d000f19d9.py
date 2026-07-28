@blueprint.route('/authorized/<remote_app>/')...
"""docstring"""
if remote_app not in handlers:
return abort(404)
return handlers[remote_app]()
