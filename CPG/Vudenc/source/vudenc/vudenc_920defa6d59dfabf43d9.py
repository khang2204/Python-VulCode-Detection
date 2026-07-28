@blueprint.route('/login/<remote_app>/')...
"""docstring"""
if remote_app not in oauth.remote_apps:
return abort(404)
callback_url = url_for('.authorized', remote_app=remote_app, next=request.
    args.get('next') or request.referrer or None, _external=True)
return oauth.remote_apps[remote_app].authorize(callback=callback_url)
