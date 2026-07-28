default_preferences = {'mode': 'light'}


@app.before_request
def before_request():
    preferences = request.cookies.get('preferences')
    if preferences is None:
        preferences = default_preferences
    else:
        preferences = loads(b64decode(preferences))

    g.preferences = preferences


@app.after_request
def after_request(response: Response) -> Response:
    if request.cookies.get('preferences') is None:
        preferences = default_preferences
        response.set_cookie('preferences',
                            b64encode(dumps(preferences)).decode())
