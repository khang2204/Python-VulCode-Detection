@app.before_request
def before_request():
    g.user = current_user
    g.session = session
    g.path = request.path


@app.after_request
def after_request(response):
    xss_protection_enabled = session.get('xss_protection_enabled', False)
    if not xss_protection_enabled:
        response.headers['X-XSS-Protection'] = 0

    return response


@app.route('/')
def index():
    """Create an index of all available sandboxes"""
    # Get all paths and endpoints defined under the "Sandboxes" blueprint, and place them on the index
    rules = [(rule.rule, rule.endpoint.split(".")[1]) for rule in app.url_map.iter_rules()
             if rule.endpoint.startswith('sandboxes')]
