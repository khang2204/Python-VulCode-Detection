@blueprint.route('/signup/<remote_app>/', methods=['GET', 'POST'])...
"""docstring"""
if remote_app not in signup_handlers:
return abort(404)
res = signup_handlers[remote_app]['view']()
return abort(404) if res is None else res
