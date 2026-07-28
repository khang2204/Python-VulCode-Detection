@bp.route('/logout')...
flask.g.user = None
flask.session.permanent = False
flask.session.modified = False
response = flask.make_response(flask.redirect(redirect_url()))
response.set_cookie(app.session_cookie_name, expires=0)
return response
