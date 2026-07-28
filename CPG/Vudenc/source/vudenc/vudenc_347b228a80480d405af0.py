@blueprint.route('/disconnect/<remote_app>/')...
"""docstring"""
if remote_app not in disconnect_handlers:
return abort(404)
return disconnect_handlers[remote_app]()
