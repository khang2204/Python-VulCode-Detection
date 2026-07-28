def pnf(e):
    template = '''<html>
    <head>
    <title>Error</title>
    </head>
    <body>
    <h1>Oops that page doesn't exist!!</h1>
    <h3>%s</h3>
    </body>
    </html>
    ''' % request.url

    return render_template_string(template, dir = dir, help = help, locals = locals),404

def has_no_empty_params(rule):
    default = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(default) >= len(arguments)

@app.route('/', methods = ['GET'])
def sitemap():
    links = []
    for rule in app.url_map.iter_rules():
